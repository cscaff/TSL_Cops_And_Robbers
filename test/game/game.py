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
        self.robber_pos = (1, 1)  # fixed for now

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

        # draw the robber
        rx, ry = self.robber_pos
        rect = pygame.Rect(
            rx * self.cell_size + 50,
            ry * self.cell_size + 50,
            self.cell_size - self.padding,
            self.cell_size - self.padding
        )
        pygame.draw.rect(self.screen, (255, 0, 0), rect)  # red square


        # status text
        status = "Click to place the cop" if self.game_state == "placing_cop" else "Animating..."
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
            self.game_state = "done"
            self.draw_grid()

    def animate_chase_step(self):
        # one step of the chase animation
        if not hasattr(self, 'animation_state'):
            self.animation_state = 0
            self.animation_x, self.animation_y = self.cop_pos
            self.animation_counter = 0

        if self.animation_counter >= 200:
            # finished animation
            return False

        # compute next position
        out = updateState({
            "currentState": self.animation_state,
            "Cop.x": self.animation_x,
            "Cop.y": self.animation_y,
            "Robber.x": self.robber_pos[0],
            "Robber.y": self.robber_pos[1]
        })
        self.animation_state = out["currentState"]
        self.animation_x = out["Cop.x"]
        self.animation_y = out["Cop.y"]
        self.cop_pos = (self.animation_x, self.animation_y)      

        # redraw after each step
        self.draw_grid()

        # render text
        state_text = self.font.render(f"State: {self.animation_state}", True, (0, 0, 0))
        x_text = self.font.render(f"X: {self.animation_x}", True, (0, 0, 0))
        y_text = self.font.render(f"Y: {self.animation_y}", True, (0, 0, 0))

        # blit text to screen (positioned next to grid)
        self.screen.blit(state_text, (10, self.height - 70))
        self.screen.blit(x_text, (10, self.height - 50))
        self.screen.blit(y_text, (10, self.height - 30))

        # update display
        pygame.display.flip()

         # check if cop caught the robber
        if self.cop_pos == self.robber_pos:
            # draw the cop square again on top of the robber
            rx, ry = self.robber_pos
            rect = pygame.Rect(
                rx * self.cell_size + 50,
                ry * self.cell_size + 50,
                self.cell_size - self.padding,
                self.cell_size - self.padding
            )
            pygame.draw.rect(self.screen, self.BLUE, rect)  # blue on top of red

            # display win message
            win_text = self.font.render("Cop caught the robber! You win!", True, (0, 128, 0))
            self.screen.blit(win_text, (50, 10))
            pygame.display.flip()
            time.sleep(2)  # pause so user can see message
            return False  # stop animation

        self.animation_counter += 1
        return True

    def run(self):
        running = True
        animating = False

        while running:
            # inside the while running loop
          current_time = time.time()
          if self.game_state == "done":
              if not animating:
                  animating = True
                  self.animation_state = 0
                  self.animation_x, self.animation_y = self.cop_pos
                  self.animation_counter = 0
                  self.last_step_time = current_time
              else:
                  if current_time - self.last_step_time >= self.step_interval:
                      still_animating = self.animate_chase_step()
                      self.last_step_time = current_time
                      if not still_animating:
                          running = False  # animation finished
          for evt in pygame.event.get():
              if evt.type == pygame.QUIT:
                  running = False
              elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1:
                  self.handle_click(evt.pos)
              elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_SPACE:
                  if self.game_state == "done":
                      if not animating:
                          animating = True  # start animation
                      else:
                          still_animating = self.animate_chase_step()
                          if not still_animating:
                              running = False  # animation finished
                  else:
                      # other game states if needed
                      self.draw_grid()
        #   pygame.time.delay(1000)
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