# *********************************************************************
# *                                                                   *
# *  Name:         Jack Vadasdi                                       *
# *  Class:        Computer Science II                                *
# *  Date:         9/30/2026                                          *
# *                                                                   *
# *********************************************************************
# *  Description:                                                     *
# *      tic tac toe game where x always goes first                   *
# *      with replays and a scoreboard                                *
# *                                                                   *
# *********************************************************************
# *  Bugs:                                                            *
# *      N/A as far as I am aware                                     *
# *                                                                   *
# *********************************************************************
def play_game():
    """Run the full tic-tac-toe session, playing repeated games until the user quits.

    Keeps a running scoreboard across games, resets the board before each
    game, and asks the players whether to play again after each one.

    Args:
        None

    Returns:
        None
    """
    scores = {"x": 0, "o": 0, "draws": 0}
    while True:
        board = [["1", "2", "3"],
                 ["4", "5", "6"],
                 ["7", "8", "9"]]
        display_board(board)
        result = gameloop(board)
        update_score(scores, result)
        display_score(scores)
        if not play_again():
            break
    print("Game Over")


def display_board(board):
    """Print the tic-tac-toe board to the console.

    Args:
        board (list[list[str]]): A 3x3 grid where each cell holds either a
            square number ("1"-"9") or a player mark ("x" or "o").

    Returns:
        None
    """
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---+---+---")


def get_player_move(board, player):
    """Prompt a player for a square and place their mark on the board.

    Keeps asking until the player enters a valid number from 1 to 9 that
    refers to a square that has not already been taken.

    Args:
        board (list[list[str]]): A 3x3 grid of the current game state. It is
            modified in place.
        player (str): The mark of the player whose turn it is ("x" or "o").

    Returns:
        list[list[str]]: The board after the player's mark has been placed.
    """
    while True:
        inputmove = input(f"Where would you like to play {player}? 1 to 9: ")
        if inputmove not in list("123456789") or inputmove == "":
            print("Please enter a number from 1 to 9.")
            continue
        for row in range(3):
            for column in range(3):
                if board[row][column] == inputmove:
                    board[row][column] = player
                    return board
        print("That square is already taken. Try again.")


def is_draw(board):
    """Check whether the board is completely filled.

    Args:
        board (list[list[str]]): A 3x3 grid of the current game state.

    Returns:
        bool: True if all nine squares contain an "x" or an "o", otherwise False.
    """
    counter = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == "x" or board[row][column] == "o":
                counter = counter + 1
    return counter == 9


def check_winner(board):
    """Determine whether a player has three in a row.

    Checks every row, column, and both diagonals for three matching marks.

    Args:
        board (list[list[str]]): A 3x3 grid of the current game state.

    Returns:
        str | None: The winning mark ("x" or "o") if there is a winner,
        otherwise None.
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]
    # Columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            return board[0][column]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def update_score(scores, result):
    """Record the outcome of a finished game in the scoreboard.

    Args:
        scores (dict[str, int]): The running totals with the keys "x", "o",
            and "draws". It is modified in place.
        result (str): The outcome of the game: "x", "o", or "draw".

    Returns:
        None
    """
    if result == "draw":
        scores["draws"] = scores["draws"] + 1
    else:
        scores[result] = scores[result] + 1


def display_score(scores):
    """Print the current scoreboard to the console.

    Args:
        scores (dict[str, int]): The running totals with the keys "x", "o",
            and "draws".

    Returns:
        None
    """
    print("\n--- Scoreboard ---")
    print(f"x wins: {scores['x']}")
    print(f"o wins: {scores['o']}")
    print(f"Draws:  {scores['draws']}")
    print("------------------\n")


def play_again():
    """Ask the players whether they want to play another game.

    Keeps asking until the user answers with a recognized yes or no.
    Accepts "y", "yes", "n", and "no" in any letter case.

    Args:
        None

    Returns:
        bool: True if the players want to play again, False if they want to quit.
    """
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer == "y" or answer == "yes":
            print("")
            return True
        if answer == "n" or answer == "no":
            return False
        print("Please type y or n.")


def gameloop(board):
    """Play a single game of tic-tac-toe from start to finish.

    Alternates turns between "x" (who goes first) and "o", displaying the
    board after each move, until someone wins or the board fills up.

    Args:
        board (list[list[str]]): A 3x3 grid for the new game. It is modified
            in place as moves are made.

    Returns:
        str: The result of the game: "x" or "o" for a win, or "draw".
    """
    turns = 0
    while True:
        if turns % 2 == 0:
            player = "x"
        else:
            player = "o"
        get_player_move(board, player)
        display_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return winner
        if is_draw(board):
            print("It's a draw!")
            return "draw"
        turns = turns + 1
play_game()