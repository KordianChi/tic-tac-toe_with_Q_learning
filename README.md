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

## Q-learning agent

The first strategy in the project is a Q-learning agent, which creates a Q-table by playing 50,000 games of Tic-Tac-Toe. The Q-table is essentially a matrix where each row corresponds to a particular state of the game, and each column corresponds to an action that the agent can take in that state. The entries in the table represent the expected cumulative reward that the agent can receive by taking that action in that state.

During the training process, the agent updates the Q-table after each move it makes based on the Bellman equation. The Bellman equation essentially states that the expected reward for taking an action in a particular state should be equal to the immediate reward for that action plus the expected reward for the next state, discounted by a factor gamma. This equation helps the agent to learn which actions are better to take in each state and thus make better decisions during the game.

After the Q-table is trained, the agent can use it to make decisions during the game. In each state, the agent simply looks up the row corresponding to the current state in the Q-table and chooses the action with the highest expected cumulative reward. By doing this, the agent is able to play Tic-Tac-Toe at a very high level, as it has learned the optimal strategies for each state of the game.

## Neural network agent


![pic 1](https://github.com/KordianChi/tic-tac-toe_with_Q_learning/blob/main/model.png)

The second agent, which is a neural network, was trained on a much smaller dataset of 500 games. This network was built with linear dense layers, which means that each neuron in a given layer is connected to every neuron in the previous and next layer. This allows the network to learn complex relationships between input (game state array) and output (Q-value prediction for each possible action).

In the case of the second agent, instead of creating a Q-table, the neural network was trained to predict Q-values for each possible game state. Similar to the first agent, these values were calculated based on the Bellman equation. When the network is tested, it predicts the Q-values for each possible action based on the current game state, and then selects the action with the highest Q-value.

However, it is important to note that despite being trained on a much smaller dataset than the first agent, this neural network was able to effectively beat the random player and the player using a naive strategy. Unfortunately, compared to the Q-table generated by the first agent, the neural network was much less effective and struggled to beat the player using a Q-table based on 50,000 games.
![pic 2](https://github.com/KordianChi/tic-tac-toe_with_Q_learning/blob/main/loss_plot.png)

## Tests results

Below is a table showing the probabilities of game outcomes between the given agents (10,000 games for each).Columns represent the player who makes the first move, while rows correspond to the player who makes the second move. First number is probability O (first player win), second for O lose, and last for draw.

|          | Q_learning | Neural_network | Random | Naive |
| -------- | -------- | -------- | -------- | -------- |
| Q_learning|   0.0, 0.0, 1.0    |    0.0, 1.0, 0.0    |    0.07, 0.73,	0.2    |    0.0, 1.0, 0.0     |
| Neural_network |    1.0, 0.0, 0.0    |    0.0, 1.0, 0.0     |    0.11, 0.47, 0.41    |    0.0, 0.67, 0.33     |
| Random |    0.96, 0.0, 0.04   |    0.88, 0.04, 0.08    |    0.37, 0.28, 0.35    |    NA   |
| Naive |    1.0, 0.0, 0.0   |    1.0, 0.0, 0.0   |    NA  |    0.45, 0.27, 0.27    |
