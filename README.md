# Mastermind

## Overview
This is an implementation of the classic code-breaker game called Mastermind. The goal is to correctly guess the secret combination 
of a randomly-generated color sequence within the allotted amount of attempts. After each guess, the player will be given clues that 
will indicate whether they chose a correct color or, better yet, a correct color and its correct location within the sequence. 

It'll take logical thinking and a little bit of luck to crack the secret combination. Prove that you are a Mastermind!


## Project Specifications
Technologies used: Python, Pygame for GUI elements, random.org API for random number generation

Code Structure:
* Uses OOP principles to abstract away and encapsulate functions.
* A main function is used to setup the game, maintain the game loop, and to end the game when needed.
* There are two classes used in the code: the Board class and the Game class.
* The Board class is used to initialize the visual representation of the game-- i.e., its GUI. It contains
  functions that draw the various board components based on the settings provided by the player.
* The Game class is used to to handle player actions, provide feedback to the player in the form of clues, 
  and checks if the game has been won or lost. 
* An 'assets' directory is used to store GUI elements such as icons, the game background, and music.
* A 'constants' python file is used to set global constants that control meta settings; it is also where
  assets are loaded through pygame and assigned to variables for ease of use. 

Implementations:
* Title Page with interactive buttons: start game, edit game settings, or quit.
* Game buttons that returns the player to the title page, toggles the music on/off, or redos their current guess
* Game settings that allows a player to change the difficulty and the maximum amount of attempts per game
* A colorful and responsive GUI


## How to Run
0. Make sure you have Python version 3.x installed.
1. Download and unzip this repository into your preferred directory. 
2. Using a terminal, change directory (cd) until you are in the root of this Mastermind directory. 
3. In the terminal, type 'python3 main.py' to begin.


## Screenshots
<img src="https://i.ibb.co/XFK5nq6/title.png" width="40%" /> <img src="https://i.ibb.co/hMKHYWL/gamesettings.png" width="39.6%" />

<img src="https://i.ibb.co/n08n77G/board.png" width="40%" /> <img src="https://i.ibb.co/LddjWqy/components.png" width="40%" />

<img src="https://i.ibb.co/x5NMwGC/clues.png" width="40%" /> <img src="https://i.ibb.co/k4sjpS4/lose-game.png" width="40%" />

<img src="https://i.ibb.co/bKdDg8H/lose-screen.png" width="40%" /> <img src="https://i.ibb.co/Q8qpRbv/win-screen.png" width="40%" />


