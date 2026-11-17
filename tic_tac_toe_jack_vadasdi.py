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
# *  Log:                                                             *
# *      V1.1 updated line documentation                              *
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
    scores = {"x": 0, "o": 0, "draws": 0}   #defines the scoreboard dictionary with keys and values
    while True:                             #infinite loop
        board = [["1", "2", "3"],           #define list of lists for boards
                 ["4", "5", "6"],
                 ["7", "8", "9"]]
        display_board(board)                #run display_board to print board
        result = gameloop(board)            #define results using gameloop
        update_score(scores, result)        #run update_score
        display_score(scores)               #run display_score to print scores
        if not play_again():                #check if game is over
            break                           #break infinite loop
    print("Game Over")                      #game over


def display_board(board):
    """Print the tic-tac-toe board to the console.

    Args:
        board (list[list[str]]): A 3x3 grid where each cell holds either a
            square number ("1"-"9") or a player mark ("x" or "o").

    Returns:
        None
    """
    for row in range(3):
        print(" " + " | ".join(board[row])) #print board row
        if row < 2:
            print("---+---+---")            #print divider row


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
        inputmove = input(f"Where would you like to play {player}? 1 to 9: ")   #ask where player would like to play
        if inputmove not in list("123456789") or inputmove == "":               #check if inputmove is a number or not
            print("Please enter a number from 1 to 9.")                         #print error message
            continue                                                            #repeat the question
        for row in range(3):                                                    #check each row and column to place the player's move
            for column in range(3):
                if board[row][column] == inputmove:                             #if spot on board equals the inputted move
                    board[row][column] = player                                 #set the spot equal to the current player's turn (x or o)
                    return board                                                #return the updated board
        print("That square is already taken. Try again.")                       #error message for repeated squares


def is_draw(board):
    """Check whether the board is completely filled.

    Args:
        board (list[list[str]]): A 3x3 grid of the current game state.

    Returns:
        bool: True if all nine squares contain an "x" or an "o", otherwise False.
    """
    counter = 0
    for row in range(3):                                                       #check rows and columns for locations of x and o to determin draw
        for column in range(3):
            if board[row][column] == "x" or board[row][column] == "o":         #if the spot is x or o, one tile has been played
                counter = counter + 1                                          #add one to the counter for each played tile
    return counter == 9                                                        #return counter == 9 to signal a draw


def check_winner(board):
    """Determine whether a player has three in a row.

    Checks every row, column, and both diagonals for three matching marks.

    Args:
        board (list[list[str]]): A 3x3 grid of the current game state.

    Returns:
        str | None: The winning mark ("x" or "o") if there is a winner,
        otherwise None.
    """
    for row in range(3):                                        #check all possible win conditions
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
        scores["draws"] = scores["draws"] + 1 #update draws key in dictionary
    else:
        scores[result] = scores[result] + 1 #increase the winner(result)'s score by 1 in their respective dictionary key


def display_score(scores):
    """Print the current scoreboard to the console.

    Args:
        scores (dict[str, int]): The running totals with the keys "x", "o",
            and "draws".

    Returns:
        None
    """
    print("\n--- Scoreboard ---")               #print scoreboard
    print(f"x wins: {scores['x']}")             #use scores dictionary to pull value of "x"
    print(f"o wins: {scores['o']}")             #use dictionary to pull number of O wins
    print(f"Draws:  {scores['draws']}")         #use dictionary to pill number of draws
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
        answer = input("Play again? (y/n): ").strip().lower()   #check play again and remove whitespaces and force lower case
        if answer == "y" or answer == "yes":                    #if loop to determine whether to continue game
            print("")                                           #print empty row
            return True                                         #return boolean
        if answer == "n" or answer == "no":                     #if players do not want to play again
            return False                                        #end game signal
        print("Please type y or n.")                            #error message for inappropriate answer


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
        if turns % 2 == 0:                 #check if turns is a multiple of 2 
            player = "x"                   #if yes then it is X's turn
        else:                              #if it turns is an odd number then O's turn
            player = "o"
        get_player_move(board, player)     #run get_player_move
        display_board(board)               #run display_board
        winner = check_winner(board)       #check if the winner is X or O or a draw
        if winner:                         #if there is a winner
            print(f"{winner} wins!")       #print the winner
            return winner                  #return winner variable
        if is_draw(board):                 #if draw
            print("It's a draw!")          #print draw message
            return "draw"
        turns = turns + 1                  #add one to turns
play_game()