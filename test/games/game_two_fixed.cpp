#include "/opt/homebrew/opt/raylib/include/raylib.h"
#include <math.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdatomic.h>
#include <unistd.h>

#include "../src/controller/controller_two_fixed.c"

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

    robber_x = 0;
    robber_y = 3;

    while (!WindowShouldClose()) {
        // --- Check for capture ---
        // bool caught = (cop_x == robber_x && cop_y == robber_y);

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
        DrawRectangle(robber_two_x * CELL_SIZE, robber_two_y * CELL_SIZE, CELL_SIZE, CELL_SIZE, RED);

        EndDrawing();
    }

    CloseWindow();
    return 0;
}
