
#initialize the tic tac toe board

board = ["1","2","3","4","5","6","7","8","9"]

# function to display the board

def display_board():
    print(f"{board[0]}  |  {board[1]}  | {board[2]}")
    print("-------------")
    print(f"{board[3]}  |  {board[4]}  | {board[5]}")
    print("-------------")
    print(f"{board[6]}  |  {board[7]}  | {board[8]}")


# function to get user input and place their symbol on the board

def player_move(player):
    while True:
        move = input(f"Player {player}, enter a number (1-9) to place your mark: ")
        if move in board:
            board[int(move) -1] = player
            break
        else:
            print("Invalid move! Try again.")

# function to check for a win

def check_winner(player):
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8], # horizontal wins
        [0,3,6],[1,4,7],[2,5,8], # vertical wins
        [0,4,8],[2,4,6],         # diagonal

    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]]==board[combo[2]] == player: # it check invividual list to they are same or not
            return True
    return False

#main function to run


def play_game():
    display_board()
    current_player = "X"

    for i in range(9):
        player_move(current_player)
        display_board()

        if check_winner(current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Its a tie")

# start the game

play_game()