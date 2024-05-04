global n 
n = 4

def display(board):
    for row in board:
        print(row)
    print("\n\n")

def isSafe(board, row, col):

    for k in range(n):
        if board[k][col] == 1:
            return False
    
    for k in range(1, n):
        if all(0 <= x < n for x in [row-k, col-k]):
            if board[row-k][col-k] == 1:
                return False
        
        if all(0 <= x < n for x in [row-k, col+k]):
            if board[row-k][col+k] == 1:
                return False
        
    return True


def n_queens(board, row):
    if row == n:
        display(board)
        return
    
    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1         # Place the Queen

            n_queens(board, row+1)      # Recursively explore the child

            board[row][col] = 0         # Upon reaching a dead-end, back-track and reset
                                        # all the queens placed during exploration back to 0.


board = [[0 for i in range(n)] for i in range(n)]
n_queens(board, 0)




