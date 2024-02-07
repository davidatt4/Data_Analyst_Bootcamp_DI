# Tic Tac Toe 
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input! Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def check_win(board, player):
   
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

  
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def play():
  
    board = [[" " for _ in range(3)] for _ in range(3)]

    display_board(board)

    
    for turn in range(9):
        player = "X" if turn % 2 == 0 else "O"
        row, col = player_input(player)

        
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Invalid move! The chosen position is already filled.")
            turn -= 1  

        display_board(board)

        
        if check_win(board, player):
            print(f"Player {player} wins!")
            break

    else:
        print("It's a tie!")
play()
