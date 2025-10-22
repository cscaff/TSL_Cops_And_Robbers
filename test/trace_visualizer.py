#!/usr/bin/env python3
import pygame
import sys
import math
import re
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

pygame.init()

WINDOW_WIDTH = 2000
WINDOW_HEIGHT = 1000
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 255)
GRID_GRAY = (60, 60, 60)
LIGHT_GRAY = (170, 170, 170)
DARK_BLUE = (10, 10, 42)
NEON_GREEN = (57, 255, 20)

STATE_COLORS_PALETTE = [CYAN, YELLOW, MAGENTA, GREEN, ORANGE, PURPLE]
GRID_SIZE = 20

@dataclass
class Transition:
    target: int
    conditions: Dict[str, Optional[bool]]  # None => don't care
    def matches(self, ap_values: Dict[str, bool]) -> bool:
        for ap, required in self.conditions.items():
            if required is not None and ap_values.get(ap, False) != required:
                return False
        return True

@dataclass
class State:
    id: int
    transitions: List[Transition]
    position: Tuple[int, int] = (0, 0)

class HOAAutomaton:
    def __init__(
        self,
        ap_names: List[str],
        outputs_idx: List[int],
        start_state: int,
        num_states: int,
        states_transitions: Dict[int, List[Transition]],
    ):
        self.ap_names = ap_names[:]
        self.outputs_idx = sorted(outputs_idx)
        self.outputs = [ap_names[i] for i in self.outputs_idx]
        self.inputs = [n for i, n in enumerate(ap_names) if i not in self.outputs_idx]
        self.aps = ap_names[:]
        self.initial_state = start_state
        self.current_state = start_state
        self.states: Dict[int, State] = {i: State(i, []) for i in range(num_states)}
        for sid, trs in states_transitions.items():
            self.states[sid].transitions = trs
        self.ap_values = {ap: False for ap in self.aps}
        self.state_colors = {i: STATE_COLORS_PALETTE[i % len(STATE_COLORS_PALETTE)] for i in range(num_states)}
        self._calculate_positions()

    def _calculate_positions(self):
        state_w, state_h = 160, 180
        reserve_right = 320
        usable_w = WINDOW_WIDTH - reserve_right
        n = len(self.states)
        total_w = n * state_w
        positions: List[Tuple[int, int]] = []
        if total_w <= usable_w:
            left_margin = (usable_w - total_w) // 2
            y = (WINDOW_HEIGHT - state_h) // 2
            for i in range(n):
                positions.append((left_margin + i * state_w, y))
        else:
            cols = max(1, usable_w // state_w)
            rows = math.ceil(n / cols)
            top_margin = (WINDOW_HEIGHT - rows * state_h) // 2
            for idx in range(n):
                r = idx // cols
                c = idx % cols
                row_items = min(cols, n - r * cols)
                row_left = (usable_w - row_items * state_w) // 2
                positions.append((row_left + c * state_w, top_margin + r * state_h))
        for i, pos in enumerate(positions):
            if i in self.states:
                self.states[i].position = pos

    def step(self) -> Optional[int]:
        current = self.states[self.current_state]
        for t in current.transitions:
            if t.matches(self.ap_values):
                self.current_state = t.target
                return t.target
        return None

    def reset(self):
        self.current_state = self.initial_state

    def get_matching_transitions(self) -> List[Tuple[int, Transition]]:
        cur = self.states[self.current_state]
        return [(self.current_state, t) for t in cur.transitions if t.matches(self.ap_values)]

# -------- HOA parsing --------
def parse_ap_line(line: str) -> List[str]:
    quoted = re.findall(r'"([^"]+)"', line)
    if quoted:
        return quoted
    m = re.search(r'AP:\s*(\d+)', line)
    n = int(m.group(1)) if m else 0
    return [str(i) for i in range(n)]

def parse_label_to_conditions(label: str, ap_names: List[str]) -> Dict[str, Optional[bool]]:
    cond: Dict[str, Optional[bool]] = {ap: None for ap in ap_names}
    s = label.strip()
    if s in ("t", "True", "true"):
        return cond
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1]
    if not s:
        return cond
    for p in s.split('&'):
        p = p.strip()
        if not p or p == "t":
            continue
        neg = p.startswith('!')
        name = p[1:] if neg else p
        if name.isdigit():
            idx = int(name)
            if 0 <= idx < len(ap_names):
                cond[ap_names[idx]] = not neg
        else:
            try:
                idx = ap_names.index(name)
                cond[ap_names[idx]] = not neg
            except ValueError:
                pass
    return cond

def load_hoa(path: str) -> HOAAutomaton:
    with open(path, 'r') as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    ap_names: List[str] = []
    controllable_idx: List[int] = []
    start_state = 0
    num_states = 0
    in_body = False
    cur_state: Optional[int] = None
    states_transitions: Dict[int, List[Transition]] = {}

    for ln in lines:
        if ln.startswith("AP:"):
            ap_names = parse_ap_line(ln)
        elif ln.startswith("controllable-AP:"):
            controllable_idx = [int(x) for x in re.findall(r'(\d+)', ln)]
        elif ln.startswith("Start:"):
            start_state = int(re.findall(r'(\d+)', ln)[0])
        elif ln.startswith("States:"):
            num_states = int(re.findall(r'(\d+)', ln)[0])
        elif ln == "--BODY--":
            in_body = True
        elif ln == "--END--":
            break
        elif in_body:
            if ln.startswith("State:"):
                cur_state = int(re.findall(r'(\d+)', ln)[0])
                states_transitions.setdefault(cur_state, [])
            elif ln.startswith("["):
                m = re.match(r'\[(.+?)\]\s+(-?\d+)', ln)
                if m and cur_state is not None:
                    label = m.group(1)
                    target = int(m.group(2))
                    cond = parse_label_to_conditions(label, ap_names)
                    states_transitions[cur_state].append(Transition(target=target, conditions=cond))

    for i in range(num_states):
        states_transitions.setdefault(i, [])
    return HOAAutomaton(ap_names, controllable_idx, start_state, num_states, states_transitions)

# -------- Visualizer --------
class ArcadeVisualizer:
    def __init__(self, automaton: HOAAutomaton):
        self.automaton = automaton
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("")
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.Font(None, 18)
        self.animation_timer = 0
        self.transition_flash_timer = 0
        self.new_state_flash = None

        # Controller: outputs TOP row, inputs BOTTOM row
        self.controller_buttons: Dict[str, pygame.Rect] = {}
        self._layout_controller()

        self.state_colors = getattr(self.automaton, "state_colors", None)

    def _layout_controller(self):
        panel_x = WINDOW_WIDTH - 280
        panel_y = 50
        panel_w = 260
        gap = 12
        inner_pad = 12

        outs = self.automaton.outputs
        ins = self.automaton.inputs
        max_cols = max(len(outs), len(ins)) if max(len(outs), len(ins)) > 0 else 1

        btn_w = max(40, min(80, int((panel_w - inner_pad * 2 - (max_cols - 1) * gap) / max_cols)))
        btn_h = btn_w
        panel_h = inner_pad * 2 + btn_h * 2 + gap
        self.panel_rect = pygame.Rect(panel_x, panel_y, panel_w, panel_h)

        y_top = panel_y + inner_pad
        y_bot = y_top + btn_h + gap

        def row_start_x(count):
            inner_w = panel_w - inner_pad * 2
            row_width = count * btn_w + (count - 1) * gap if count > 0 else 0
            return panel_x + inner_pad + (inner_w - row_width) // 2

        self.controller_buttons.clear()
        x0 = row_start_x(len(outs))
        for i, ap in enumerate(outs):
            r = pygame.Rect(x0 + i * (btn_w + gap), y_top, btn_w, btn_h)
            self.controller_buttons[ap] = r

        x1 = row_start_x(len(ins))
        for i, ap in enumerate(ins):
            r = pygame.Rect(x1 + i * (btn_w + gap), y_bot, btn_w, btn_h)
            self.controller_buttons[ap] = r

    def draw_gradient_background(self):
        for y in range(WINDOW_HEIGHT):
            ci = int(20 + 10 * math.sin(y * 0.01 + self.animation_timer * 0.001))
            pygame.draw.line(self.screen, (ci // 4, 0, ci), (0, y), (WINDOW_WIDTH, y))

    def draw_grid_pattern(self, rect, exclude_rects=[]):
        for x in range(rect.left, rect.right, GRID_SIZE):
            for y in range(rect.top, rect.bottom, GRID_SIZE):
                r = pygame.Rect(x, y, GRID_SIZE - 1, GRID_SIZE - 1)
                if any(er.colliderect(r) for er in exclude_rects):
                    continue
                pygame.draw.rect(self.screen, GRID_GRAY, r, 1)

    def draw_state(self, state: State, is_current: bool):
        x, y = state.position
        state_width = 160
        state_height = 180
        color = self.state_colors[state.id] if self.state_colors else CYAN

        if is_current or (self.new_state_flash == state.id and self.transition_flash_timer > 0):
            for i in range(6):
                alpha = 100 - i * 8
                s = pygame.Surface((state_width + i * 4, state_height + i * 4))
                s.set_alpha(alpha)
                s.fill(color)
                self.screen.blit(s, (x - 5 - i * 2, y - 5 - i * 2))
            bw = 5
        else:
            bw = 3

        rect = pygame.Rect(x, y, state_width, state_height)
        pygame.draw.rect(self.screen, BLACK, rect)
        pygame.draw.rect(self.screen, color, rect, bw)

        # dynamic transition grid (no gaps between cells)
        outer_pad = 8
        cell_gap = 0
        inner_w = state_width - 2 * outer_pad
        inner_h = state_height - 2 * outer_pad
        n = len(state.transitions)
        if n == 0:
            return

        cols = max(1, int(math.ceil(math.sqrt(n))))
        def cell_size(c):
            r = int(math.ceil(n / c))
            return (inner_w - (c - 1) * cell_gap) / c, (inner_h - (r - 1) * cell_gap) / r, r
        while True:
            cw, ch, rows = cell_size(cols)
            if cw >= 34 and ch >= 30:
                break
            if cols > 1: cols -= 1
            else: break

        trs_rects = []
        outs = self.automaton.outputs
        ins = self.automaton.inputs
        o, i_cnt = len(outs), len(ins)

        for idx, t in enumerate(state.transitions):
            c = idx % cols
            r = idx // cols
            cw, ch, rows = cell_size(cols)
            tx = x + outer_pad + c * (cw + cell_gap)
            ty = y + outer_pad + r * (ch + cell_gap)
            tr = pygame.Rect(int(tx), int(ty), int(cw), int(ch))
            trs_rects.append(tr)

            is_match = is_current and t.matches(self.automaton.ap_values)
            target_color = self.state_colors[t.target] if self.state_colors else YELLOW
            bg = BLACK if not is_match else (20, 20, 20)
            pygame.draw.rect(self.screen, bg, tr)
            pygame.draw.rect(self.screen, target_color, tr, 4 if is_match else 3)

            # AP rows (adjacent squares, no gaps)
            left_pad = 8
            avail_w = tr.width - 2 * left_pad
            max_cols = max(1, o, i_cnt)
            dot = max(10, min(22, int(avail_w / max_cols)))  # adjacent
            top_y = tr.y + 6
            bot_y = tr.y + tr.height - dot - 6

            def row_start_x(count):
                row_w = count * dot
                return tr.x + left_pad + (avail_w - row_w) // 2

            # outputs (top)
            x0 = row_start_x(o)
            for k, ap in enumerate(outs):
                cx = x0 + k * dot
                cell = pygame.Rect(cx, top_y, dot, dot)
                v = t.conditions.get(ap, None)
                colr = GREEN if v is True else RED if v is False else LIGHT_GRAY
                pygame.draw.rect(self.screen, colr, cell)
                pygame.draw.rect(self.screen, GRID_GRAY, cell, 1)

            # divider
            pygame.draw.line(self.screen, GRID_GRAY,
                             (tr.x + 5, tr.y + tr.height // 2),
                             (tr.x + tr.width - 5, tr.y + tr.height // 2), 1)

            # inputs (bottom)
            x1 = row_start_x(i_cnt)
            for k, ap in enumerate(ins):
                cx = x1 + k * dot
                cell = pygame.Rect(cx, bot_y, dot, dot)
                v = t.conditions.get(ap, None)
                colr = GREEN if v is True else RED if v is False else LIGHT_GRAY
                pygame.draw.rect(self.screen, colr, cell)
                pygame.draw.rect(self.screen, GRID_GRAY, cell, 1)

        inner_rect = pygame.Rect(x + 3, y + 3, state_width - 6, state_height - 6)
        self.draw_grid_pattern(inner_rect, trs_rects)

    def draw_controller(self):
        pygame.draw.rect(self.screen, DARK_BLUE, self.panel_rect)
        pygame.draw.rect(self.screen, CYAN, self.panel_rect, 3)
        for ap, rect in self.controller_buttons.items():
            val = self.automaton.ap_values.get(ap, False)
            color = GREEN if val else RED
            is_output = ap in self.automaton.outputs
            border_color = NEON_GREEN if (val and is_output) else (150, 0, 0) if not val else WHITE
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, border_color, rect, 3)
            # Labels removed intentionally to keep controller buttons unlabeled
        

    def handle_click(self, pos):
        for ap, rect in self.controller_buttons.items():
            if rect.collidepoint(pos):
                self.automaton.ap_values[ap] = not self.automaton.ap_values[ap]
            
    def step_automaton(self):
        old = self.automaton.current_state
        new = self.automaton.step()
        if new is not None and new != old:
            self.new_state_flash = new
            self.transition_flash_timer = 20
        return new

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            self.animation_timer += dt
            if self.transition_flash_timer > 0:
                self.transition_flash_timer -= 1
                if self.transition_flash_timer == 0:
                    self.new_state_flash = None

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                    elif e.key == pygame.K_SPACE:
                        State=self.step_automaton()
                    elif e.key == pygame.K_r:
                        self.automaton.reset()
                        self.transition_flash_timer = 0
                        self.new_state_flash = None
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(e.pos)

            for y in range(WINDOW_HEIGHT):
                ci = int(20 + 10 * math.sin(y * 0.01 + self.animation_timer * 0.001))
                pygame.draw.line(self.screen, (ci // 4, 0, ci), (0, y), (WINDOW_WIDTH, y))

            for sid, st in self.automaton.states.items():
                self.draw_state(st, sid == self.automaton.current_state)

            self.draw_controller()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

def main():
    if len(sys.argv) < 2:
        print("Usage: python hoa_visualizer.py <path_to_hoa_file>")
        sys.exit(1)
    hoa_path = sys.argv[1]
    automaton = load_hoa(hoa_path)
    ArcadeVisualizer(automaton).run()

if __name__ == "__main__":
    main()
