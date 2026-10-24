# Tic-Tac-Toe Game
# Two-player console game.
# Player 1 uses X and Player 2 uses O.

def display_board(board):
    """Display the current board."""
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def get_move(board, current_player):
    """Ask the current player for a valid, empty cell."""
    while True:
        choice = input(
            "Player " + current_player + ", choose a cell (1-9): "
        ).strip()

        # Reject empty input.
        if choice == "":
            print("Input cannot be empty. Try again.")
            continue

        # Reject letters or other non-numeric input.
        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        # Reject numbers outside the range 1-9.
        position = int(choice)
        if position < 1 or position > 9:
            print("Invalid number. Choose a cell from 1 to 9.")
            continue

        # Reject a cell that already contains X or O.
        index = position - 1
        if board[index] == "X" or board[index] == "O":
            print("That cell is already occupied. Try again.")
            continue

        return index


def check_winner(board, current_player):
    """Return True if the current player has a winning line."""
    winning_positions = [
        [0, 1, 2],  # Rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonals
        [2, 4, 6]
    ]

    for line in winning_positions:
        if (board[line[0]] == current_player and
                board[line[1]] == current_player and
                board[line[2]] == current_player):
            return True

    return False


def check_draw(board):
    """Return True when no numbered (empty) cells remain."""
    for cell in board:
        if cell != "X" and cell != "O":
            return False

    return True


def play_round():
    """Play one round and return the result: X, O, or D for draw."""
    # A fresh board is created for every round.
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    while True:
        display_board(board)
        index = get_move(board, current_player)
        board[index] = current_player

        # Check for a win immediately after a valid move.
        if check_winner(board, current_player):
            display_board(board)
            print("Player", current_player, "wins!")
            return current_player

        # Check for a draw only if nobody has won.
        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            return "D"

        # Switch players only after a valid move.
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def ask_play_again():
    """Ask whether to start another round."""
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter yes or no.")


def main():
    """Start and manage the game."""
    print("=== TIC-TAC-TOE ===")
    play_again = True

    while play_again:
        play_round()
        play_again = ask_play_again()

    print("Thanks for playing Tic-Tac-Toe!")


# Run the game when this file is started.
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGame closed. Thanks for playing!")


