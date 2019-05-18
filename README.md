# PGO_Effects_on_Assembly_Code
## A study on the effects of PGO using Hotspot VM

# The_Hobbit_Learns
## Reinforcement learning using the Q-learning approach of rewards.

## Authors
* Naveed Mahmud
* Shambo Ghosh

## The Thror's Map

![Treasure_Hunt_In_Progress](https://user-images.githubusercontent.com/35944630/57576577-53813000-7428-11e9-9973-9e3a1da330ed.png)


In this diagram (our map like environment), the RED object is our Hobbit, the ORANGE ones are the obstacles and the GREEN circle is our treasure.

## Ts

In this journey, there are "50" attempts made by Hobbit. 

In each of those attempts the Hobbit;

* ends up getting the treasure (rewards = +1), 
* reaches an obstacle (rewards = -1) 
* moves around and stays in the ground state (rewards = 0). 

The goal is to find the *optimum* path to the treasure by avoiding all the obstacles.

## Reinforcement Learning

Some of the actions the Hobbit can take are;

* Go UP
* Go DOWN
* Move LEFT
* Move RIGHT

The learning process has the following methods; 

* *Selects* an action
* *Learns* from the actions, considers the 
  * present state
  * the action it takes
  * the rewards it gets 
  * the new state it reaches
* *Checks* if state exists 


Some of the parameters of Q-Learning;

* Learning Rate = 0.01 
* Reward Decay = 0.9 

## Installation

Clone the repository and run the **Start_Hunting.py** file

## Project Structure

1. **this.py** - This script parses the assembly code 
2. **Learning_Engine.py** - Has the reinforcement learning logic.
3. **Start_Hunting.py** - Entry to the adventure.

## References

1. https://www.ibm.com/developerworks/library/j-jtp12214/
2. https://blog.overops.com/java-on-steroids-5-super-useful-jit-optimization-techniques/
3. https://www.oracle.com/technetwork/java/javase/tech/vmoptions-jsp-140102.html



