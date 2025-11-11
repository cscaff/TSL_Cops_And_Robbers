#!/usr/bin/env bash
set -euo pipefail

# Usage: ./update_and_test.sh /path/to/spec.tsl
# Default target file (relative to current dir)
TARGET="./src/controller/controller.c"

SPEC_PATH="./src/spec/spec.tslmt"

if [[ -z "$SPEC_PATH" ]]; then
  echo "Usage: $0 /path/to/spec.tsl [target_file]"
  exit 2
fi

# Optional override of target file
if [[ -n "${2:-}" ]]; then
  TARGET="$2"
fi

# Ensure directory exists
mkdir -p "$(dirname "$TARGET")"

# Run issy and write stdout into controller.c (overwrite)
# If you want to append, use >> instead of >
echo "Running: issy --tslmt --solve --synt $SPEC_PATH"
if ! issy --tslmt --solve --synt "$SPEC_PATH" >"$TARGET" 2> >(tee /tmp/issy.err >&2); then
  echo "issy failed — see /tmp/issy.err for stderr output"
  exit 3
fi

# Optional: add markers around the injected output (uncomment to use)
# { echo "/* --- injected: begin --- */"; issy --tslmt --solve --synt "$SPEC_PATH"; echo "/* --- injected: end --- */"; } >"$TARGET"

echo "Wrote controller to $TARGET"

# Run tests that use controller.c (replace with your actual test command)
# examples:
#   - if you have a test script: ./run_controller_tests.sh
#   - if you use make: make -C ./test file_name_test
#   - if tests are a binary: ./test/run_tests "$TARGET"
# Here is a placeholder:
if [[ -x "./run_controller_tests.sh" ]]; then
  echo "Running ./run_controller_tests.sh..."
  ./run_controller_tests.sh "$TARGET"
else
  echo "No test script found at ./run_controller_tests.sh — replace this with your test command"
fi
