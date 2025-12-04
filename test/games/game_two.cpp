#include "/opt/homebrew/opt/raylib/include/raylib.h"
#include <math.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdatomic.h>
#include <unistd.h>

#include "../src/controller/controller_two.c"

#define GRID_SIZE 2
#define CELL_SIZE 80
#define SCREEN_SIZE (GRID_SIZE * CELL_SIZE)

typedef struct {
    int x, y;
} Player;

void* controller_thread(void* arg) {
    step_controller(); // synthesized controller
    return NULL;
}

int main(void) {
    pthread_t tid;
    pthread_create(&tid, NULL, controller_thread, NULL);

    InitWindow(SCREEN_SIZE, SCREEN_SIZE, "Cop and Robber Grid Game");
    SetTargetFPS(10);

    cop_x = 0;
    cop_y = 0;

    // Cop Two
    cop_x_two = 1;
    cop_y_two = 0;


    robber_x = GRID_SIZE - 1;
    robber_y = GRID_SIZE - 1;

    while (!WindowShouldClose()) {
        // --- Input for robber (player-controlled) ---
        if (IsKeyPressed(KEY_W)) { player_dx = 0; player_dy = -1; new_input_ready = 1; }
        if (IsKeyPressed(KEY_S)) { player_dx = 0; player_dy = 1;  new_input_ready = 1; }
        if (IsKeyPressed(KEY_A)) { player_dx = -1; player_dy = 0; new_input_ready = 1; }
        if (IsKeyPressed(KEY_D)) { player_dx = 1; player_dy = 0;  new_input_ready = 1; }


        // --- Check for capture ---
        bool caught = (cop_x == robber_x && cop_y == robber_y);

        // --- Draw ---
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Draw grid
        for (int i = 0; i <= GRID_SIZE; i++) {
            DrawLine(i * CELL_SIZE, 0, i * CELL_SIZE, SCREEN_SIZE, LIGHTGRAY);
            DrawLine(0, i * CELL_SIZE, SCREEN_SIZE, i * CELL_SIZE, LIGHTGRAY);
        }

        // Draw cop and robber
        DrawRectangle(robber_x * CELL_SIZE, robber_y * CELL_SIZE, CELL_SIZE, CELL_SIZE, RED);
        DrawRectangle(cop_x * CELL_SIZE, cop_y * CELL_SIZE, CELL_SIZE, CELL_SIZE, BLUE);
        DrawRectangle(cop_x_two * CELL_SIZE, cop_y_two * CELL_SIZE, CELL_SIZE, CELL_SIZE, BLUE);



        if (caught) {
            DrawText("CAUGHT!", SCREEN_SIZE/2 - 100, SCREEN_SIZE/2 - 20, 40, BLACK);
        }

        EndDrawing();

        if (caught) {
            WaitTime(2.0);
            break;
        }
    }

    CloseWindow();
    return 0;
}
