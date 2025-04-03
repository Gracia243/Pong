# Pong for Windows

## Description
This is a simple Pong game implemented in Python using the `turtle` and `pygame` libraries. The game consists of two paddles and a bouncing ball. Players control the paddles to hit the ball back and forth. The first player to reach 20 points wins the game.

## Features
- Two-player gameplay
- Paddle movement using keyboard controls
- Ball physics with speed increase on paddle collision
- Score tracking and display
- Sound effects for ball collisions

## Requirements
Ensure you have Python installed on your system. Additionally, install the required dependencies:

```bash
pip install pygame
```

## How to Play
- **Player A (Left Paddle):**
  - Move Up: Press `Z`
  - Move Down: Press `S`
- **Player B (Right Paddle):**
  - Move Up: Press `Up Arrow`
  - Move Down: Press `Down Arrow`
- The game ends when one player reaches 20 points.

## Running the Game
To run the game, execute the following command in your terminal or command prompt:

```bash
python pong.py
```

## Game Rules
- The ball bounces off the paddles and the top/bottom walls.
- If a player misses the ball, the opponent scores a point.
- The game speeds up as the ball hits the paddles.
- The first player to reach 20 points wins.

## Sound Effects
Make sure you have the `bounce.wav` file in the same directory as the script. This file is used for the ball's bounce sound effect.

## Notes
- The game is implemented using `turtle` for graphics and `pygame` for sound.
- Ensure that your system supports `pygame.mixer` for sound functionality.

## License
This project is for educational purposes and can be freely modified and distributed.

## Author
Gracia Lukoji

