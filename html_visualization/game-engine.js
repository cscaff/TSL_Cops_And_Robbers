// Cops and Robbers Game Engine

class GameEngine {
    constructor() {
        this.gridSize = 4; // 4x4 grid (0-3 for each axis)
        this.cellSize = 150;
        this.padding = 100;

        this.cop = { x: 3, y: 0 };
        this.robber = { x: 0, y: 0 };
        this.currentState = 0;
        this.step = 0;

        this.running = false;
        this.controller = null;
        this.speed = 500; // milliseconds per step
        this.intervalId = null;

        this.canvas = null;
        this.ctx = null;
    }

    setCanvas(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
    }

    setController(controllerFunc) {
        this.controller = controllerFunc;
        this.log('Controller loaded successfully', 'success');
    }

    loadControllerFromString(codeString) {
        try {
            // Create a function from the string
            const wrappedCode = `
                ${codeString}
                return updateState;
            `;
            const func = new Function(wrappedCode)();
            this.setController(func);
            return true;
        } catch (error) {
            this.log('Error loading controller: ' + error.message, 'error');
            return false;
        }
    }

    reset() {
        this.stop();
        this.cop = { x: 3, y: 0 };
        this.robber = { x: 0, y: 0 };
        this.currentState = 0;
        this.step = 0;
        this.log('Game reset', 'success');
        this.updateUI();
        this.render();
    }

    start() {
        if (!this.controller) {
            this.log('No controller loaded!', 'error');
            return;
        }

        if (this.running) return;

        this.running = true;
        this.log('Simulation started', 'success');
        this.intervalId = setInterval(() => this.executeStep(), this.speed);
        this.updateUI();
    }

    stop() {
        if (!this.running) return;

        this.running = false;
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
        this.log('Simulation stopped', 'success');
        this.updateUI();
    }

    executeStep() {
        if (!this.controller) {
            this.stop();
            this.log('No controller loaded!', 'error');
            return;
        }

        // Check if cop caught robber
        if (this.cop.x === this.robber.x && this.cop.y === this.robber.y) {
            this.stop();
            this.log('Cop caught the robber!', 'success');
            this.updateUI();
            return;
        }

        try {
            // Call the controller
            const inputs = {
                currentState: this.currentState,
                Robber_x: this.robber.x,
                Robber_y: this.robber.y,
                Cop_x: this.cop.x,
                Cop_y: this.cop.y
            };

            const outputs = this.controller(inputs);

            // Update state
            this.currentState = outputs.currentState ?? this.currentState;

            if (outputs.Cop_x !== undefined) this.cop.x = outputs.Cop_x;
            if (outputs.Cop_y !== undefined) this.cop.y = outputs.Cop_y;
            if (outputs.Robber_x !== undefined) this.robber.x = outputs.Robber_x;
            if (outputs.Robber_y !== undefined) this.robber.y = outputs.Robber_y;

            // Clamp positions to grid
            this.cop.x = Math.max(0, Math.min(this.gridSize - 1, this.cop.x));
            this.cop.y = Math.max(0, Math.min(this.gridSize - 1, this.cop.y));
            this.robber.x = Math.max(0, Math.min(this.gridSize - 1, this.robber.x));
            this.robber.y = Math.max(0, Math.min(this.gridSize - 1, this.robber.y));

            this.step++;
            this.log(`Step ${this.step}: Cop(${this.cop.x},${this.cop.y}) Robber(${this.robber.x},${this.robber.y}) State:${this.currentState}`);

        } catch (error) {
            this.stop();
            this.log('Controller error: ' + error.message, 'error');
        }

        this.updateUI();
        this.render();
    }

    render() {
        if (!this.ctx) return;

        const ctx = this.ctx;
        const canvas = this.canvas;

        // Clear canvas
        ctx.fillStyle = '#252526';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw grid
        ctx.strokeStyle = '#3e3e42';
        ctx.lineWidth = 2;

        for (let i = 0; i <= this.gridSize; i++) {
            // Vertical lines
            ctx.beginPath();
            ctx.moveTo(this.padding + i * this.cellSize, this.padding);
            ctx.lineTo(this.padding + i * this.cellSize, this.padding + this.gridSize * this.cellSize);
            ctx.stroke();

            // Horizontal lines
            ctx.beginPath();
            ctx.moveTo(this.padding, this.padding + i * this.cellSize);
            ctx.lineTo(this.padding + this.gridSize * this.cellSize, this.padding + i * this.cellSize);
            ctx.stroke();
        }

        // Draw coordinates
        ctx.fillStyle = '#9cdcfe';
        ctx.font = '14px Courier New';
        for (let i = 0; i < this.gridSize; i++) {
            // X coordinates
            ctx.fillText(i, this.padding + i * this.cellSize + this.cellSize / 2 - 5, this.padding - 10);
            // Y coordinates
            ctx.fillText(i, this.padding - 30, this.padding + i * this.cellSize + this.cellSize / 2 + 5);
        }

        // Draw robber (red circle)
        ctx.fillStyle = '#f48771';
        ctx.beginPath();
        ctx.arc(
            this.padding + this.robber.x * this.cellSize + this.cellSize / 2,
            this.padding + this.robber.y * this.cellSize + this.cellSize / 2,
            30,
            0,
            2 * Math.PI
        );
        ctx.fill();

        // Robber label
        ctx.fillStyle = '#1e1e1e';
        ctx.font = 'bold 16px Courier New';
        ctx.textAlign = 'center';
        ctx.fillText('R',
            this.padding + this.robber.x * this.cellSize + this.cellSize / 2,
            this.padding + this.robber.y * this.cellSize + this.cellSize / 2 + 6
        );

        // Draw cop (blue circle)
        ctx.fillStyle = '#4ec9b0';
        ctx.beginPath();
        ctx.arc(
            this.padding + this.cop.x * this.cellSize + this.cellSize / 2,
            this.padding + this.cop.y * this.cellSize + this.cellSize / 2,
            30,
            0,
            2 * Math.PI
        );
        ctx.fill();

        // Cop label
        ctx.fillStyle = '#1e1e1e';
        ctx.font = 'bold 16px Courier New';
        ctx.textAlign = 'center';
        ctx.fillText('C',
            this.padding + this.cop.x * this.cellSize + this.cellSize / 2,
            this.padding + this.cop.y * this.cellSize + this.cellSize / 2 + 6
        );

        ctx.textAlign = 'left';
    }

    updateUI() {
        // Update info panel
        document.getElementById('step').textContent = this.step;
        document.getElementById('state').textContent = this.currentState;
        document.getElementById('cop-pos').textContent = `(${this.cop.x}, ${this.cop.y})`;
        document.getElementById('robber-pos').textContent = `(${this.robber.x}, ${this.robber.y})`;

        let status = 'Ready';
        if (this.running) status = 'Running';
        else if (this.cop.x === this.robber.x && this.cop.y === this.robber.y) status = 'Caught!';
        document.getElementById('status').textContent = status;

        // Update button states
        document.getElementById('startBtn').disabled = this.running;
        document.getElementById('stepBtn').disabled = this.running;
    }

    log(message, type = 'info') {
        const logDiv = document.getElementById('log');
        const entry = document.createElement('div');
        entry.className = `log-entry ${type}`;
        const timestamp = new Date().toLocaleTimeString();
        entry.textContent = `[${timestamp}] ${message}`;
        logDiv.appendChild(entry);
        logDiv.scrollTop = logDiv.scrollHeight;

        // Keep only last 50 entries
        while (logDiv.children.length > 50) {
            logDiv.removeChild(logDiv.firstChild);
        }
    }

    setSpeed(ms) {
        this.speed = ms;
        if (this.running) {
            this.stop();
            this.start();
        }
    }
}
