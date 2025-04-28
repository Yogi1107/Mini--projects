import math

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the game is over (win or tie)
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    
    # Check if the board is full (tie)
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Minimax algorithm
def minimax(board, depth, is_maximizing_player):
    if is_game_over(board):
        if check_winner(board) == PLAYER_O:
            return 1  # AI wins
        elif check_winner(board) == PLAYER_X:
            return -1  # Player X wins
        else:
            return 0  # Tie

    if is_maximizing_player:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# Function to check the winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

# Function to find the best move for AI
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    
    return move

# Main game loop for Player vs Player
def player_vs_player():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    print("Player 1 (X) vs Player 2 (O)")
    print_board(board)
    
    while not is_game_over(board):
        # Player 1's move (Player X)
        row = int(input("Player 1, enter the row (0-2) for your move: "))
        col = int(input("Player 1, enter the column (0-2) for your move: "))
        
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_X
            print_board(board)
        else:
            print("Invalid move, try again.")
            continue
        
        if is_game_over(board):
            break
        
        # Player 2's move (Player O)
        row = int(input("Player 2, enter the row (0-2) for your move: "))
        col = int(input("Player 2, enter the column (0-2) for your move: "))
        
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_O
            print_board(board)
        else:
            print("Invalid move, try again.")
            continue
        
        if is_game_over(board):
            break
    
    # Check who won or if it's a tie
    winner = check_winner(board)
    if winner:
        print(f"Player {1 if winner == PLAYER_X else 2} wins!")
    else:
        print("It's a tie!")

# Main game loop for Player vs AI
def player_vs_ai():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    print("Player (X) vs AI (O)")
    print_board(board)
    
    while not is_game_over(board):
        # Player's move (Player X)
        row = int(input("Enter the row (0-2) for your move: "))
        col = int(input("Enter the column (0-2) for your move: "))
        
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_X
            print_board(board)
        else:
            print("Invalid move, try again.")
            continue
        
        if is_game_over(board):
            break
        
        # AI's move (Player O)
        print("AI is making its move...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_O
        print_board(board)
        
        if is_game_over(board):
            break
    
    # Check who won or if it's a tie
    winner = check_winner(board)
    if winner:
        if winner == PLAYER_X:
            print("You win!")
        elif winner == PLAYER_O:
            print("AI wins!")
    else:
        print("It's a tie!")

# Main function to choose the game mode
def main():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose game mode - Player vs Player (1) or Player vs AI (2): ")
    
    if mode == "1":
        player_vs_player()
    elif mode == "2":
        player_vs_ai()
    else:
        print("Invalid choice. Exiting the game.")

if __name__ == "__main__":
    main()
