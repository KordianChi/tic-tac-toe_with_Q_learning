# tic-tac-toe_with_Q_learning
## Introduction

This project aims to apply Q-learning algorithm in a Tic Tac Toe game. The game is implemented using Python programming language, and the Q-learning algorithm is used to train a model that can make optimal moves in the game. The project includes several functions for playing the game, such as a function for generating all possible moves, a function for updating the Q-table, and a function for selecting the best move based on the current state of the game. This project is a learning exercise and serves as a starting point for more advanced projects in the field of reinforcement learning.

This project involves using Q-learning in a tic-tac-toe game and testing the possibility of using a neural network to reproduce the Q-table based on a smaller number of games. The project serves as an exercise before taking on more advanced challenges in the field of reinforcement learning.

## Test assumptions

To test the effectiveness of the neural network, the Q-table generated from a long game (50,000) will be compared with the D-table generated from a short series of games (500). The test involves playing games with a random player, a player using a naive strategy, and between themselves. In each case, both algorithms will play 10,000 games as both O and X.

During the test, we observed the following facts:

* In the games between random players, the player who made the first move had a significant advantage.
* Both the player with the exact Q-table and the one using the neural network had an advantage over the random player, especially when they had the first move.
* The player using the naive strategy was no challenge for either of the policies.
* The player with the exact Q-table had a complete advantage over the player using the neural network.

Interestingly, the Q-table generated through the long-term game (50,000) outperformed the Q-table generated from a short series of games (500) using the neural network. One possible reason for this is that the Q-table generated through a long-term game includes more game states, leading to better coverage of the state space. In contrast, the neural network-based Q-table's accuracy was limited by the size of the dataset used to train the network. Additionally, the neural network's training algorithm may have overfit the training data, resulting in poor performance on new data. Therefore, the neural network-based Q-table was not able to outperform the Q-table generated through a long-term game.
