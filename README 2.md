# Tornado-api
## Instructions for running tic-tac-toe api
Save Dockerfile and docker-compose.yml in the same directory and run using **_docker-compose up_**

API documentation can be found here: https://tictactoe11.docs.apiary.io/#

or here: https://github.com/bpeters-cmu/Tornado-api/blob/master/apiary.apib

Tornado is configured to listen on port 80

This application is also currently running on AWS and can be accessed at 52.87.242.146:80/api/games
  
## Gameplay
The tic-tac-toe board is represented by a list data structure, with 1 representing X and 0 representing O

The positional layout of the board is as follows:

                                            0 | 1 | 2

                                            3 | 4 | 5

                                            6 | 7 | 8

Players are automatically assigned X or O and take turns based on the "nextTurn" field returned in the "Get Game By ID" api. 

Player1 is always assigned 'x' (appended to player name like so "player1-x") similarly Player2 is assigned 'o' "player2-o"

When a player gets 3 in a row, they win and the game is over, also, if the board is full and neither player has 3 in a row, the game ends in a draw
