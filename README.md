# Tic-Tac-Toe Game Using Python

## Project Description
This is a beginner-friendly, two-player Tic-Tac-Toe game that runs in the terminal.
Player 1 uses X and Player 2 uses O. Players take turns choosing a cell on a 3x3 board.

## Features
- Displays a 3x3 board after every move
- Two-player turns using the same keyboard
- Players choose a cell using numbers 1 to 9
- Input validation for empty input, letters, numbers outside 1-9, and occupied cells
- Checks all 3 rows, 3 columns, and 2 diagonals for a win
- Detects a draw when all cells are filled and nobody wins
- Offers a play-again option and resets the board for a new round
- Uses beginner-friendly Python functions, lists, loops, and conditional statements
- Handles Ctrl+C or closed input gracefully

## Requirements
- Python 3.x
- No external libraries or database are required

## How to Run
1. Open this folder in Visual Studio Code.
2. Open **Terminal > New Terminal**.
3. Run:

   ```powershell
   python tic_tac_toe.py
   ```

   If that command does not work on Windows, try:

   ```powershell
   py tic_tac_toe.py
   ```

4. Follow the instructions shown in the terminal.

## Cell Numbers
The board starts with cells numbered 1 to 9:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

Choose a number to place the current player's symbol in that cell.

## Game Rules
1. Player X starts first.
2. Players take turns choosing an empty cell.
3. The first player to make three matching symbols in a row, column, or diagonal wins.
4. If all nine cells are filled and no player wins, the round ends in a draw.
5. After each round, enter `yes` to play again or `no` to exit.

## Main Python Concepts
- Variables and data types
- Lists
- Functions
- `while` and `for` loops
- Conditional statements
- Input validation
- Basic exception handling
- String methods such as `strip()` and `lower()`

## Files
- `tic_tac_toe.py` - the Python game
- `README.md` - project description and run instructions
