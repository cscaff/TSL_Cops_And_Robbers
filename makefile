# ---------------- Compiler ----------------
CC = clang++
CFLAGS = -Wall -std=c++17 $(shell pkg-config --cflags raylib)
LDFLAGS = $(shell pkg-config --libs raylib) \
          -framework Cocoa \
          -framework IOKit \
          -framework CoreVideo


# ---------------- Raylib game ----------------
GAME_SRC = ./test/games/game.cpp
GAME_BIN = ./test/exe/cop_robber

# ---------------- Controller test ----------------
CONTROLLER = ./src/controller/controller.cpp

# ---------------- Default ----------------
.PHONY: all
all: run

# ---------------- Run everything ----------------
.PHONY: run
run: synthesize game

# ---------------- Build Raylib game ----------------
.PHONY: game
game: $(GAME_BIN)

$(GAME_BIN): $(GAME_SRC) 
	@echo ">>> Compiling Raylib game..."
	$(CC) $(CFLAGS) $(GAME_SRC) $(LDFLAGS) -o $@
	
	
# ---------------- Synthesize controller ----------------
.PHONY: synthesize
synthesize:
	@echo ">>> Running synthesis script..."
	./test/synthesize.sh
	@echo ">>> Controller generated at $(CONTROLLER)"

# ---------------- Clean ----------------
.PHONY: clean
clean:
	@echo ">>> Cleaning binaries..."
	rm -f $(GAME_BIN) $(TEST_BIN)
