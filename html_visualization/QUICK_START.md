# Quick Start Guide

## Running Your First Visualization

1. **Open the HTML file**:
   ```bash
   # From the repository root
   cd html_visualization
   # Then open index.html in your browser (or double-click it)
   ```

2. **See it in action**:
   - The page loads with a default controller already configured
   - Click the "Start" button to watch the cop chase the robber
   - The cop (blue circle marked 'C') will move toward the robber (red circle marked 'R')

3. **Control the simulation**:
   - **Start/Stop**: Space bar or Start button
   - **Single Step**: S key or Step button
   - **Reset**: R key or Reset button
   - **Speed**: Use the slider to adjust animation speed

## Loading Your Own Controller

### Option 1: Manual Conversion (Recommended)

1. Look at your Python controller's `updateState` function
2. Follow this pattern to convert it:

**Python:**
```python
def updateState(_inputs_and_cells):
    currentState, Robber.x, Cop.x = itemgetter("currentState", "Robber.x", "Cop.x")(_inputs_and_cells)

    if currentState == 0:
        if Cop.x > Robber.x:
            _next_Cop.x = Cop.x - 1
            currentState = 1

    return {"currentState": currentState, "Cop.x": _next_Cop.x}
```

**JavaScript:**
```javascript
function updateState(inputs) {
    const { currentState, Robber_x, Cop_x } = inputs;
    let next_Cop_x = Cop_x;
    let nextState = currentState;

    if (currentState === 0) {
        if (Cop_x > Robber_x) {
            next_Cop_x = Cop_x - 1;
            nextState = 1;
        }
    }

    return { currentState: nextState, Cop_x: next_Cop_x };
}
```

3. Copy your converted JavaScript into the text area on the page
4. Click "Load Controller"
5. Click "Start" to run it

### Option 2: Use the Converter Script

```bash
# Convert a Python controller
python html_visualization/convert_controller.py test/debugging/test.py

# Copy the output and paste it into the web page
```

**Note**: The converter handles basic patterns but may need manual fixes for complex logic.

## Key Conversion Rules

1. **Variable names**: Replace dots with underscores
   - `Cop.x` → `Cop_x`
   - `Robber.y` → `Robber_y`

2. **Operators**:
   - `and` → `&&`
   - `or` → `||`
   - `==` → `===`
   - `!=` → `!==`

3. **Variables**:
   - `_next_Cop.x` → `next_Cop_x`
   - `currentState` → `nextState` (for assignments)

4. **Input/Output**:
   - Input: `inputs.Cop_x`, `inputs.Robber_x`, etc.
   - Output: Return object with updated values

## Example: Simple "Move Toward" Controller

```javascript
function updateState(inputs) {
    const { currentState, Robber_x, Cop_x } = inputs;

    let next_Cop_x = Cop_x;
    let nextState = currentState;

    // Simple logic: move cop toward robber
    if (Cop_x > Robber_x) {
        next_Cop_x = Cop_x - 1;
    } else if (Cop_x < Robber_x) {
        next_Cop_x = Cop_x + 1;
    }

    return {
        currentState: nextState,
        Cop_x: next_Cop_x
    };
}
```

## Troubleshooting

**Q: Controller not working?**
A: Check the log at the bottom for errors. Common issues:
- Missing `return` statement
- Wrong variable names (dots instead of underscores)
- Syntax errors (missing braces, semicolons)

**Q: Cop/Robber not moving?**
A: Make sure you're returning the updated position:
```javascript
return { currentState: nextState, Cop_x: next_Cop_x };
```

**Q: How do I debug?**
A: Add console.log statements in your controller:
```javascript
console.log('State:', currentState, 'Cop:', Cop_x, 'Robber:', Robber_x);
```
Then open browser DevTools (F12) to see the output.

## What's Next?

- Try modifying the example controller to use different strategies
- Add Y-axis movement (2D instead of 1D)
- Implement robber movement logic
- Experiment with different state machines

For more details, see the full [README.md](README.md).
