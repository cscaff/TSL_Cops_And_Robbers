// Example controller converted from test/debugging/test.py
// This controller moves the cop toward the robber in a simple 1D scenario

function updateState(inputs) {
    const { currentState, Robber_x, Cop_x } = inputs;

    let next_Cop_x = Cop_x;
    let nextState = currentState;

    if (currentState === 0) {
        if ((Cop_x !== Robber_x) && (Cop_x === 3) && (Robber_x === 0) && (Cop_x > Robber_x)) {
            next_Cop_x = Cop_x - 1;
            nextState = 1;
        } else if ((Cop_x !== Robber_x) && (Cop_x === 3) && (Robber_x === 0) && (Cop_x <= Robber_x)) {
            next_Cop_x = Cop_x;
            nextState = 2;
        } else if ((Cop_x === Robber_x)) {
            nextState = 3;
        } else if (Cop_x !== 3) {
            nextState = 3;
        } else if (Robber_x !== 0) {
            nextState = 3;
        }
    } else if (currentState === 1) {
        if ((Cop_x !== Robber_x) && (Robber_x === 0) && (Cop_x > Robber_x)) {
            next_Cop_x = Cop_x - 1;
            nextState = 2;
        } else if ((Cop_x === Robber_x)) {
            nextState = 3;
        } else if ((Robber_x !== 0)) {
            nextState = 3;
        }
    } else if (currentState === 2) {
        if ((Cop_x !== Robber_x) && (Robber_x === 0)) {
            next_Cop_x = Cop_x - 1;
            nextState = 2;
        } else if ((Cop_x === Robber_x)) {
            nextState = 3;
        } else if (Robber_x !== 0) {
            nextState = 3;
        }
    } else if (currentState === 3) {
        // End state - do nothing
        nextState = 3;
    }

    return {
        currentState: nextState,
        Cop_x: next_Cop_x
    };
}
