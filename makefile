# ---- Configuration ----
SCRIPT = ./run.sh
TARGET = ./src/controller/controller.c
TEST_SRC = ./test/game.c
TEST_BIN = ./test/controller_test

# ---- Default target ----
.PHONY: all
all: run

# ---- Run Issy + test ----
.PHONY: run
run:
	@echo ">>> Running Issy and tests..."
	$(SCRIPT)
	@echo ">>> Done."

# ---- Compile and run test only ----
.PHONY: test
test: $(TEST_BIN)
	@echo ">>> Running test harness..."
	$(TEST_BIN)

# ---- Build test binary ----
$(TEST_BIN): $(TEST_SRC) $(TARGET)
	@echo ">>> Compiling test harness..."
	gcc -Wall -Wextra -O2 -o $@ $(TEST_SRC)

# ---- Clean ----
.PHONY: clean
clean:
	@echo ">>> Cleaning test binaries..."
	rm -f $(TEST_BIN)
