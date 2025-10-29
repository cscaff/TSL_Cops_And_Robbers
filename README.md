# Cops And Robbers TSL Specification

This project is a work in progress. To run the specification, you need TSL installed from [here](https://github.com/Barnard-PL-Labs/tsltools). To run the program, utilize the following:

## Dependency Installation
```
pip install -r requirements.txt
```

## Running the Specification

Assuming TSL is saved to your system path, you can run:
```
python3 ./test/run.py
```
## Current Progress

Legacy Spec illustrates a spec that synthesizes a cop agent that is guaranteed to chase after a robber controlled by user input.

The next step is to move away from a cop restricted to a certain strategy:

```
  // Cop Movement
  (Cop.x < Robber.x) -> [Cop.x <- Cop.moveR(Cop.x)];
  (Cop.x > Robber.x) -> [Cop.x <- Cop.moveL(Cop.x)];
  (Cop.y > Robber.y) -> [Cop.y <- Cop.moveU(Cop.y)];
  (Cop.y < Robber.y) -> [Cop.y <- Cop.moveD(Cop.y)];
```

Rather, we want to make use of the idea of a **Cop Win Graph** dictated by **dismantlablity**. Our Cops and Robbers Grid can be defined as a **king's graph**. Because two path graphs are dismantlable and dismantlablity is closed under strong product of graphs, we know that king's graphs are also dismantlable. 

Thus, the new task is to identify if we can specify the constraints that inform the synthesis tool our graph is a king's graph and is thus dismantlable.