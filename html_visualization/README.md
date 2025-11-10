# HTML Visualization for Cops and Robbers Controllers

This directory contains a browser-based visualization system for running and testing your Cops and Robbers controllers without needing pygame.

## Quick Start

1. **Open the visualization**: Simply open `index.html` in your web browser (double-click the file or open it with your browser)

2. **Load a controller**:
   - Either paste JavaScript controller code directly into the text area
   - Or convert a Python controller first (see below)

3. **Run the simulation**:
   - Click "Start" to run continuously
   - Click "Step" to execute one step at a time
   - Click "Reset" to reset the game state
   - Use the speed slider to adjust simulation speed

## Converting Python Controllers to JavaScript

Use the provided converter script to transform your Python controllers:

```bash
# Convert a Python controller and save to file
python html_visualization/convert_controller.py test/debugging/test.py -o html_visualization/controller.js

# Or just print to stdout
python html_visualization/convert_controller.py test/debugging/test.py
```

Then copy the output and paste it into the controller text area in the HTML page.

## Keyboard Shortcuts

- **Space**: Start/Stop simulation
- **S**: Execute single step
- **R**: Reset game

## Controller Format

Your JavaScript controller should have this structure:

```javascript
function updateState(inputs) {
    // inputs contains:
    // - currentState: current FSM state
    // - Cop_x, Cop_y: cop position
    // - Robber_x, Robber_y: robber position

    let next_Cop_x = inputs.Cop_x;
    let next_Cop_y = inputs.Cop_y;
    let nextState = inputs.currentState;

    // Your controller logic here
    if (inputs.currentState === 0) {
        if (inputs.Cop_x > inputs.Robber_x) {
            next_Cop_x = inputs.Cop_x - 1;
            nextState = 1;
        }
    }

    // Return updated values
    return {
        currentState: nextState,
        Cop_x: next_Cop_x,
        // Cop_y: next_Cop_y,  // Include if your controller updates Y
        // Robber_x: next_Robber_x,  // Include if your controller moves robber
        // Robber_y: next_Robber_y
    };
}
```

## Features

- **Grid Visualization**: 4x4 grid with coordinate labels
- **Real-time Updates**: See the cop (blue) and robber (red) move in real-time
- **Step-by-step Control**: Step through your controller logic one move at a time
- **State Tracking**: View current step, FSM state, and positions
- **Log Output**: See a log of all actions and events
- **Speed Control**: Adjust simulation speed from 100ms to 2000ms per step

## Example: Testing the Default Controller

1. Open `index.html` in your browser
2. The default controller is already loaded (simplified version from test.py)
3. Click "Start" to watch the cop move toward the robber
4. Observe how the state transitions work

## Troubleshooting

**Controller not working?**
- Check the log at the bottom for error messages
- Make sure your `updateState` function returns an object with the correct keys
- Verify that returned positions are within grid bounds (0-3)

**Python conversion issues?**
- The converter handles basic patterns - complex Python may need manual adjustment
- Check that variable names are converted (e.g., `Cop.x` → `Cop_x`)
- Ensure boolean operators are converted (`and` → `&&`, `or` → `||`)

**Grid not rendering?**
- Make sure all three files are in the same directory
- Check browser console (F12) for JavaScript errors

## File Structure

```
html_visualization/
├── index.html              # Main HTML page
├── game-engine.js          # Game logic and rendering
├── visualization.js        # UI event handlers
├── convert_controller.py   # Python to JS converter
└── README.md              # This file
```

## Notes

- The game runs on a 4x4 grid (coordinates 0-3 on each axis)
- Default starting positions: Cop at (3,0), Robber at (0,0)
- The simulation stops when the cop catches the robber (same position)
- All controller logic runs in the browser - no server needed!
