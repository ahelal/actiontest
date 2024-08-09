import random

# Initialize the game board
board = [' ' for _ in range(9)]

def loadGame():
    user_input = input("Enter game filename: ")
    with open(user_input, 'r') as file:
        content = file.read()
        return  content

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw():
    return ' ' not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move():
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            break

def xo_game():
    print("Welcome to Tic-Tac-Toe!")
    display_board()

    while True:
        player_move()
        display_board()
        if check_win('X'):
            print("Congratulations! You win!..")
            break
        if check_draw():
            print("It's a draw!")
            break

        computer_move()
        display_board()
        if check_win('O'):
            print("Computer wins! Better luck next time.")
            break
        if check_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    xo_game()
