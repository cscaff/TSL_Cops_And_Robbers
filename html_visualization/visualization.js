// UI and Event Handlers

const game = new GameEngine();

// Initialize on load
window.addEventListener('DOMContentLoaded', () => {
    // Setup canvas
    const canvas = document.getElementById('gameCanvas');
    game.setCanvas(canvas);

    // Load default controller from textarea
    const controllerCode = document.getElementById('controllerCode').value;
    game.loadControllerFromString(controllerCode);

    // Initial render
    game.render();
    game.updateUI();

    // Setup event listeners
    document.getElementById('startBtn').addEventListener('click', () => {
        game.start();
    });

    document.getElementById('stepBtn').addEventListener('click', () => {
        game.executeStep();
    });

    document.getElementById('resetBtn').addEventListener('click', () => {
        game.reset();
    });

    document.getElementById('loadControllerBtn').addEventListener('click', () => {
        const controllerCode = document.getElementById('controllerCode').value;
        if (game.loadControllerFromString(controllerCode)) {
            game.reset();
        }
    });

    // Speed slider
    const speedSlider = document.getElementById('speedSlider');
    const speedValue = document.getElementById('speedValue');

    speedSlider.addEventListener('input', (e) => {
        const speed = parseInt(e.target.value);
        speedValue.textContent = speed;
        game.setSpeed(speed);
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.key === ' ') {
            e.preventDefault();
            if (game.running) {
                game.stop();
            } else {
                game.start();
            }
        } else if (e.key === 's' || e.key === 'S') {
            e.preventDefault();
            game.executeStep();
        } else if (e.key === 'r' || e.key === 'R') {
            e.preventDefault();
            game.reset();
        }
    });

    game.log('Visualization ready. Use Space to start/stop, S to step, R to reset', 'success');
});
