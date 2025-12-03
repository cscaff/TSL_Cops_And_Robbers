# ---------------- Compiler ----------------
CC = clang++
CFLAGS = -Wall -std=c++17 $(shell pkg-config --cflags raylib)
LDFLAGS = $(shell pkg-config --libs raylib) \
          -framework Cocoa \
          -framework IOKit \
          -framework CoreVideo


# ---------------- Raylib game ----------------
GAME_SRC = ./test/game.cpp
GAME_BIN = cop_robber

# ---------------- Controller test ----------------
CONTROLLER = ./src/controller/controller.cpp
TEST_SRC = ./test/game.cpp
TEST_BIN = ./test/controller_test
SCRIPT = ./test/synthesize.sh

# ---------------- Default ----------------
.PHONY: all
all: run

# ---------------- Build & run Raylib game ----------------
.PHONY: game
game: $(GAME_BIN)

$(GAME_BIN): $(GAME_SRC) 
	@echo ">>> Compiling Raylib game..."
	$(CC) $(CFLAGS) $(GAME_SRC) $(LDFLAGS) -o $@
	
	

# ---------------- Synthesize controller ----------------
.PHONY: synthesize
synthesize: $(CONTROLLER)

$(CONTROLLER):
	@echo ">>> Running synthesis script..."
	$(SCRIPT)
	@echo ">>> Controller generated at $(CONTROLLER)"

# ---------------- Compile & run test harness ----------------
.PHONY: test
test: $(TEST_BIN)
	@echo ">>> Running test harness..."
	./$(TEST_BIN)

$(TEST_BIN): $(TEST_SRC) $(CONTROLLER)
	@echo ">>> Compiling test harness..."
	$(CC) -Wall -std=c99 -o $@ $(TEST_SRC) $(CONTROLLER)

# ---------------- Run everything ----------------
.PHONY: run
run: synthesize test

# ---------------- Clean ----------------
.PHONY: clean
clean:
	@echo ">>> Cleaning binaries..."
	rm -f $(GAME_BIN) $(TEST_BIN)
