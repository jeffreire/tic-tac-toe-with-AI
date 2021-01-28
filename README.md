# Tic-tac-toe
Tic-tac-toe, one of the most classic and simple games to play. Surely you must have played with your friends at some point in your life.
With the advancement of technology, it allowed us to use this game as a model to validate the artificial intelligence algorithm called **MINIMAX**.

Therefore, this algorithm is the main key in this tic-tac-toe.

# Problem

To get a better understanding of the concepts of the search algorithms, we were challenged to implement a tic-tac-toe using the classic **MINIMAX** 
algorithm and getting its best performance.

# Objective

To obtain the best performance using the MINMAX algorithm in a competition of two agents in the face of the tic-tac-toe game, where an agent only wants 
to maximize his victory points, but for the other side, what matters is to maximize the defeat points.

# Solution

To solve this problem with 100% success. We need to create the following variables:

- **X = player 1**
- **O = player 2**
  
if **X** wins you will get **+1**, but if you win, you’ll get **-1**, in the event of a tie, the score will be **0**.
after defining the awards, we declare the following functions:

**initial_state()** - Function that will receive the initial state of the board.

**player()** - Function that will receive the current state of the board and will return the turn of the next player/agent.

**actions()** - Function that will receive the current board and will return the possible actions that the agent can perform in his turn.

**result()** - Function that will receive the status of the current board and the agent's action. Returning the board with the current actions.

**winner()** - Function that will receive the board and check if there will be any sequence that will determine if the game is over, tied or a victory for any of the agents. Returning **X**, **O** or none.

**terminal()** - You will receive the board and check whether the game is over or not, if it is over it will return **TRUE**, otherwise it will return **FALSE**.

**utility()** - Function that receives the final state of the board and will return **1** if **X** won and **-1** if **O** won.

**minimax()** - Function that contains the implemented **MINIMAX AlGORITHM**.

**minimax_aux()** - Function that will make the best search possible to obtain the expected result.


