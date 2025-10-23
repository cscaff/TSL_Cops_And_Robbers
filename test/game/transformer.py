import ast 
import astor

class TraceInjector(ast.NodeTransformer):
    def __init__(self, module_name="tracer"):
        self.module_name = module_name
        self.in_state_block = False

    # Ensures we visit function definitions.
    def visit_FunctionDef(self, node):
        # Ensures we visit nested structures.
        node = self.generic_visit(node)
        return node
    
    def visit_If(self, node):
        # Detect whether this is a top-level FSM state selector
        is_state_if = (
            isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "currentState"
        )

        # Case 1: Top Level State Condition
        if is_state_if and not self.in_state_block:
            # Temporarily set context flag to True while visiting its body
            self.in_state_block = True
            node = self.generic_visit(node)
            self.in_state_block = False
            return node

        # Case 2: This is a nested conditional (inside a state)
        if self.in_state_block:
            # Visit its body as usual
            self.generic_visit(node)

            # Convert AST test to string
            cond_str = astor.to_source(node.test).strip()

            # Log actions taken per event
            actions = []
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    for t in stmt.targets:
                        target_str = astor.to_source(t).strip()
                        value_str = astor.to_source(stmt.value).strip()
                        actions.append(f"{target_str}={value_str}")
            
            # Inject logging call
            trace_call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id='log_condition', ctx=ast.Load()),
                    args=[
                        ast.Constant(cond_str),
                        ast.Name(id='currentState', ctx=ast.Load()),
                        ast.Constant(actions)
                        ],
                    keywords=[]
                )
            )
            
            node.body.insert(0, trace_call)

        return node

def transformer(code_str):
    """Accepts Python code as a string and returns instrumented code as a string"""
    tree = ast.parse(code_str)
    tree = TraceInjector().visit(tree)
    ast.fix_missing_locations(tree)
    source = astor.to_source(tree)

    # Dependencies:
    dep = """
from datetime import datetime
from operator import itemgetter
from entities import Robber, Cop, _next_Cop

def log_condition(cond_str, current_state, actions):
    print(f"- - - - - - - - - - - - - - - - -")
    print(f"t = {datetime.now().strftime("%H:%M:%S")}")
    print(f"[TRACE] Current State = {current_state}")
    print(f"[TRACE] Chosen Next Event Condition: {cond_str}")
    print(f"[TRACE]   Actions to Perform: [{'\\n'.join(actions)}]")\n
"""

    source = dep + source

    return source
