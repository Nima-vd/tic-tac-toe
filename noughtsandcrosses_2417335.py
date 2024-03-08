import json
import random
import os.path

random.seed()

def draw_board(board):
    """
    Visually represents the current state of the Tic tac Toe game board in 3*3 grid format.
    Prints the board in a 3x3 grid with dashes(-) and pipes(|).
    X denotes the player move and O denotes computer move.
    """
    print('-------------')
    for row in board:
        temp = '| '
        for mark in row:
            temp += mark + ' | '
        print(temp)
        print('-------------')

def welcome(board):
    """
    Prints a welcome message and displays the initial empty board.
    """
    print("Welcome to 'Unbeatable Noughts and Crosses'!")
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    """
    Initializes the board with empty spaces.
    returns 3*3 grid filed with spaces.
    """
    return [[' ' for _ in range(3)] for _ in range(3)]

def get_player_move(board):
    """
    Prompts the user to input a number corresponding to the square they want.
    """
    while True:
        player_choice = input("Choose your square (1-9): ")
        if not player_choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        choice = int(player_choice)
        if not 1 <= choi0ce <= 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        row = (choice - 1) // 3
        col = (choice - 1) % 3
        if board[row][col] != ' ':
            print("Square already taken. Choose another.")
            continue
        return row, col

def choose_computer_move(board):
    """
    Chooses a random move for the computer from the list of empty spaces.
    """
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_positions)

def check_for_win(board, mark):
    """
    Checks if the player or computer has won.
    checks rows,columns, and diagonals.
    """
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    """
    Checks if the game is a draw.
    if all cells on the board are filled.
    """
    return all(cell != ' ' for row in board for cell in row)

def play_game(board):
    """
    Main game loop.
    Alternates between the player's move
    and the computer's move until the game ends.
    """
    welcome(board)
    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_for_draw(board):
            print("It's a draw!")
            break
        print("Computer's move:")
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins!")
            break

def menu():
    """
    Displays the menu options.
    prompts them to enter their choice.
    """
    print("\nMENU:")
    print("1. Play Game")
    print("2. Save Score in Leaderboard")
    print("3. Display Leaderboard")
    print("q. Quit")
    return input("Enter your choice: ")

def load_scores():
    """
    Loads the leaderboard scores from the file.
    returns the scores as a dictionary.
    """
    scores = {}
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                scores = json.load(file)
            except json.decoder.JSONDecodeError:
                print("Leaderboard file is empty.")
    else:
        print("Leaderboard file does not exist.")
    return scores

def save_score(score, name):
    """
    Saves the player's score to the leaderboard file.
    """
    scores = load_scores()
    scores[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(scores, file)
        print("Score saved successfully.")

def display_leaderboard(leaders):
    """
    Displays the leaderboard.
    """
    print("\nLEADERBOARD:")
    print("Name\tScore")
    for name, score in leaders.items():
        print(f"{name}\t{score}")

# Main program
"""
main program where the game loop runs.
Initializes the game board,display menu, and then executes corresponding actions
based on player's choice.
The loop continues until the player chooses to quit.
"""
if __name__ == "__main__":
    board = initialise_board([])
    while True:
        choice = menu()
        if choice == '1':
            play_game(board)
        elif choice == '2':
            name = input("Enter your name: ")
            save_score(1, name)  # Dummy score for now
        elif choice == '3':
            display_leaderboard(load_scores())
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")