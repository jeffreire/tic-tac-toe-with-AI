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

to solve this problem with 100% success. We need to create the following variables:

       **X = player 1**
       **O = player 2**
if X wins you will get +1, but if you win, you’ll get -1, in the event of a tie, the score will be 0.




 the following functions:

* initial_state () - Function that will receive the initial state of the board.

* player () -
Function that will receive the current state of the board and will return the turn of the next player.

* actions () - Function that will receive the current board and return the possible actions that the agent can take in his turn.
