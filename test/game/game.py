import pygame
import time

# Synthesized Controller
from controller import updateState


class GridGame:
    def __init__(self, n, m):
        pygame.init()

        self.last_step_time = 0
        self.step_interval = 0.5  # seconds


        # store dimensions and set globals for MaxX/MaxY
        self.n, self.m = n, m
        global _MAX_M, _MAX_N
        _MAX_M = m
        _MAX_N = n


        # drawing params
        self.cell_size = 50
        self.padding = 2
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.GRAY = (200, 200, 200)
        self.RED = (255, 0, 0)

        # screen setup
        self.width = self.m * self.cell_size + 100
        self.height = self.n * self.cell_size + 100
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"Grid Game ({n}×{m})")

        # only track the cop’s position as (x, y): (column, row)
        self.cop_pos = None
        self.game_state = 'placing_cop'
        self.font = pygame.font.SysFont(None, 24)

        # Robber Position (fixed for now)
        self.robber_pos = None

        self.robberDirection = {
            "moveL": False,
            "moveR": False,
            "moveU": False,
            "moveD": False,
            "stayX": False,
            "stayY": False
        }

        # Current Turn
        self.turn = "robber"

        # Animation State
        self.animation_state = 0

    def draw_grid(self):
        # clear background
        self.screen.fill(self.GRAY)

        # draw empty cells
        for row in range(self.n):
            for col in range(self.m):
                rect = pygame.Rect(
                    col * self.cell_size + 50,
                    row * self.cell_size + 50,
                    self.cell_size - self.padding,
                    self.cell_size - self.padding
                )
                pygame.draw.rect(self.screen, self.WHITE, rect)

        # draw the cop at its current position (if placed)
        if self.cop_pos:
            x, y = self.cop_pos  # x=column, y=row
            rect = pygame.Rect(
                x * self.cell_size + 50,
                y * self.cell_size + 50,
                self.cell_size - self.padding,
                self.cell_size - self.padding
            )

            pygame.draw.rect(self.screen, self.BLUE, rect)
        
        if self.robber_pos:
            rx, ry = self.robber_pos
            rect = pygame.Rect(
                rx * self.cell_size + 50,
                ry * self.cell_size + 50,
                self.cell_size - self.padding,
                self.cell_size - self.padding
            )
            
            if self.game_state != "capture":
                pygame.draw.rect(self.screen, self.RED, rect)
            else:
                pygame.draw.rect(self.screen, self.BLUE, rect)

        # status text
        if self.game_state == "placing_cop":
            status = "Click to place the cop"
        elif self.game_state == "placing_robber":
            status = "Click to place the robber"
        else:
            status = "Animating..."
        text_surf = self.font.render(status, True, self.BLUE)
        self.screen.blit(text_surf, (10, 10))

        pygame.display.flip()

    def get_cell_from_pos(self, pos):
        x, y = pos
        if x < 50 or y < 50:
            return None
        col = (x - 50) // self.cell_size
        row = (y - 50) // self.cell_size
        if 0 <= row < self.n and 0 <= col < self.m:
            return (col, row)  # return as (x, y)
        return None

    def handle_click(self, pos):
        cell = self.get_cell_from_pos(pos)
        if cell and self.game_state == "placing_cop":
            self.cop_pos = cell  # now (x, y)
            self.draw_grid()
            self.game_state = "placing_robber"
        elif cell and self.game_state == "placing_robber":
            self.robber_pos = cell  # now (x, y)
            self.draw_grid()
            self.game_state = "running"



    def move_robber(self, dx, dy):
        rx, ry = self.robber_pos
        new_x = rx + dx
        new_y = ry + dy

        # Ensure robber stays inside bounds
        if 0 <= new_x < self.m and 0 <= new_y < self.n:
            self.robber_pos = (new_x, new_y)
            self.turn = "cop"
            self.draw_grid()
            self.check_game_end()

        # Record Robber Movement State
        if new_x > rx:
            self.robberDirection["moveR"] = True
        if new_x < rx:
            self.robberDirection["moveL"] = True
        if new_y > ry:
            self.robberDirection["moveD"] = True
        if new_y < ry:
            self.robberDirection["moveU"] = True
        if new_y == ry:
            self.robberDirection["stayY"] = True
        if new_x == rx:
            self.robberDirection["stayX"] = True

    def cop_move(self):
        if not self.cop_pos:
            return
        
        out = updateState({
            "currentState": self.animation_state,
            "MaxX": self.m - 1,
            "MinY": 0,
            "Robber.moveD": self.robberDirection["moveD"],
            "Robber.moveL": self.robberDirection["moveL"],
            "Robber.moveR": self.robberDirection["moveR"],
            "Robber.moveU": self.robberDirection["moveU"],
            "Robber.stayX": self.robberDirection["stayX"],
            "Robber.stayY": self.robberDirection["stayY"],
            "Cop.x": self.cop_pos[0],
            "Cop.y": self.cop_pos[1],
            "Robber.x": self.robber_pos[0],
            "Robber.y": self.robber_pos[1]
        })

        # Reset Robber Movement State
        self.robberDirection = {
            "moveL": False,
            "moveR": False,
            "moveU": False,
            "moveD": False,
            "stayX": False,
            "stayY": False
        }

        self.animation_state = out["currentState"]
        self.cop_pos = (out["Cop.x"], out["Cop.y"])
        self.turn = "robber"
        self.draw_grid()
        self.check_game_end()

    def check_game_end(self):
        if self.cop_pos == self.robber_pos:
            self.game_state = "capture"
            self.draw_grid()
            win_text = self.font.render("Cop caught the robber! Game over!", True, (0, 128, 0))
            self.screen.blit(win_text, (50, 10))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            exit()


    def run(self):
        running = True
        self.draw_grid()

        while running:
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    running = False
                elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1:
                    self.handle_click(evt.pos)
                elif evt.type == pygame.KEYDOWN:
                    if self.game_state == "running":
                        dx = dy = 0

                        keys = pygame.key.get_pressed()

                        # Vertical
                        if keys[pygame.K_w]:
                            dy -= 1
                        elif keys[pygame.K_s]:
                            dy += 1

                        # Horizontal
                        if keys[pygame.K_a]:
                            dx -= 1
                        elif keys[pygame.K_d]:
                            dx += 1

                        # Move if any direction pressed
                        self.move_robber(dx, dy)

                        # Cop moves after robber finishes
                        if self.turn == "cop":
                            self.cop_move()

            self.draw_grid()

        pygame.quit()

 

def main():
    try:
        n = int(input("Enter number of rows (N): "))
        m = int(input("Enter number of columns (M): "))
        if n <= 0 or m <= 0:
            print("Grid dimensions must be positive")
            return
        
        game = GridGame(n, m)

        game.run()

    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    main()