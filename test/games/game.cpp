#include "/opt/homebrew/opt/raylib/include/raylib.h"
#include "../../src/controller/controller.cpp"

// Threading
#include <pthread.h>
#include <chrono>
#include <thread>
#include <atomic>

// FIle I/O
#include <fstream>

// Randomization
#include <ctime>
#include <math.h>

// Grid Sizing
#define CELL_SIZE 80
#define SCREEN_SIZE (GRID_SIZE * CELL_SIZE)

void* controller_thread(void* arg) {
    step_controller(); // synthesized controller
    return NULL;
}

int write_to_file(const char* filename) {
    // String Trace
    // Append Final State
    std::string curr_trace = std::string("{\"RobberX\":") + std::to_string(robber_x) +
            ", \"RobberY\": " + std::to_string(robber_y) +
            ", \"CopX\": " + std::to_string(cop_x) +
            ", \"CopY\": " + std::to_string(cop_y) + "}\n";

    std::cout << curr_trace << std::endl;

    // Append Final State
    // trace += curr_trace;

    // Enclose Current Trace
    trace = std::string("<TRACE_START>\n") + trace + std::string("<TRACE_END>\n");

    // std::ofstream file(filename, std::ios::app);
    // if (!file.is_open()) {
    //     return -1; 
    // }
    // file << trace;
    // file.close();
    return 0;
}

// Optional Random Robber Movement Generator
void movement_generator() {
    // Block while controller reads:
    while (new_input_ready == 1) {
        usleep(1000);
    }

    int dir = rand() % 5;
    std::cout << "DIR: " << dir << std::endl;
    
    switch (dir) {
        case 0: { player_dx = 0; player_dy = -1; break;}
        case 1: { player_dx = 0; player_dy = 1; break;}
        case 2: { player_dx = -1; player_dy = 0; break;}
        case 3: { player_dx = 1; player_dy = 0; break;}
        case 4: { player_dx = 0; player_dy = 0; break;}
    }
    
    // Free Lock
    new_input_ready = 1;
}

int main(int argc, char* argv[]) {
    std::cout << "================================\nCops and Robbers\n================================" << std::endl;
    std::cout << "Press \"q\" to quit or any other key to play again!\n" << std::endl;
    
    // Thread Creation 
    pthread_t tid;
    pthread_create(&tid, NULL, controller_thread, NULL);
    
    // Initialize window once if using graphical mode
    bool use_graphics = (argc > 1 && (std::string(argv[1]) == "--play" || std::string(argv[1]) == "--watch"));
    if (use_graphics) {
        InitWindow(SCREEN_SIZE, SCREEN_SIZE, "Cop and Robber Grid Game");
        SetTargetFPS(10);
    }
    
    // Game Loop
    bool quit = false;
    while(!quit) {
        // Reset Trace
        trace.clear();

        srand(time(NULL));
        
        // Random cop position
        cop_x = rand() % GRID_SIZE;
        cop_y = rand() % GRID_SIZE;
        
        // Random robber position, ensuring different from cop
        do {
            robber_x = rand() % GRID_SIZE;
            robber_y = rand() % GRID_SIZE;
        } while (robber_x == cop_x && robber_y == cop_y);
        
        if (argc > 1 && (std::string(argv[1]) == "--trace")) {    
            while (!quit) {
                // Random Robber Movement
                movement_generator();
                
                // --- Check for capture ---
                bool caught = (cop_x == robber_x && cop_y == robber_y);
                
                // Check for capture
                if (caught) {
                    write_to_file("trace.txt");
                    std::cout << "\nCaught! Press any key to play again or 'q' to quit: ";
                    
                    char input;
                    std::cin >> input;
                    
                    if (input == 'q' || input == 'Q') {
                        quit = true;
                    }
                    break;
                }
                
                // Add a small delay to prevent busy-waiting
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
            }
        } else {        
            bool game_over = false;
            while (!WindowShouldClose() && !quit && !game_over) {
                // Quit Game
                if (IsKeyPressed(KEY_Q)) {
                    quit = true;
                    break;
                }
                
                // --- Input for robber (player-controlled) ---
                if (argc > 1 && (std::string(argv[1]) == "--play")) {
                    if (IsKeyPressed(KEY_W)) { player_dx = 0; player_dy = -1; new_input_ready = 1; }
                    if (IsKeyPressed(KEY_S)) { player_dx = 0; player_dy = 1;  new_input_ready = 1; }
                    if (IsKeyPressed(KEY_A)) { player_dx = -1; player_dy = 0; new_input_ready = 1; }
                    if (IsKeyPressed(KEY_D)) { player_dx = 1; player_dy = 0;  new_input_ready = 1; }
                } else if (argc > 1 && (std::string(argv[1]) == "--watch")) {
                    movement_generator();
                }
                
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
                
                if (caught) {
                    DrawText("CAUGHT!", SCREEN_SIZE/2 - 100, SCREEN_SIZE/2 - 20, 40, BLACK);
                    DrawText("Press any key to play again", SCREEN_SIZE/2 - 150, SCREEN_SIZE/2 + 30, 20, DARKGRAY);
                    DrawText("Press Q to quit", SCREEN_SIZE/2 - 80, SCREEN_SIZE/2 + 60, 20, DARKGRAY);
                }
                
                EndDrawing();
                
                if (caught) {
                    write_to_file("trace.txt");
                    
                    // Wait for key press
                    bool waiting = true;
                    while (waiting && !WindowShouldClose()) {
                        if (IsKeyPressed(KEY_Q)) {
                            quit = true;
                            waiting = false;
                        } else if (GetKeyPressed() != 0) {
                            // Any other key pressed - play again
                            game_over = true;
                            waiting = false;
                        }
                        
                        // Keep drawing while waiting
                        BeginDrawing();
                        ClearBackground(RAYWHITE);
                        
                        for (int i = 0; i <= GRID_SIZE; i++) {
                            DrawLine(i * CELL_SIZE, 0, i * CELL_SIZE, SCREEN_SIZE, LIGHTGRAY);
                            DrawLine(0, i * CELL_SIZE, SCREEN_SIZE, i * CELL_SIZE, LIGHTGRAY);
                        }
                        
                        DrawRectangle(robber_x * CELL_SIZE, robber_y * CELL_SIZE, CELL_SIZE, CELL_SIZE, RED);
                        DrawRectangle(cop_x * CELL_SIZE, cop_y * CELL_SIZE, CELL_SIZE, CELL_SIZE, BLUE);
                        DrawText("CAUGHT!", SCREEN_SIZE/2 - 100, SCREEN_SIZE/2 - 20, 40, BLACK);
                        DrawText("Press any key to play again", SCREEN_SIZE/2 - 150, SCREEN_SIZE/2 + 30, 20, DARKGRAY);
                        DrawText("Press Q to quit", SCREEN_SIZE/2 - 80, SCREEN_SIZE/2 + 60, 20, DARKGRAY);
                        
                        EndDrawing();
                    }
                    
                    break;
                }
            }
        }
    }
    pthread_join(tid, NULL);
    
    // Close window once at the end
    if (use_graphics) {
        CloseWindow();
    }
    
    return 0;
}