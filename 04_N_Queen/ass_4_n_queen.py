# N-Queen Problem

global n
n = 4

def display(board):
    n = len(board)
    for i in range(n):
        print(board[i])


# This will check if the square (row, col) is safe for the next Queen to be placed
 
def isSafe(board, row, col):

    # checking all squares in the given Column
    for k in range(n):
        if(board[k][col] == 1):
            return False
    
    # checking all squares in the Top-Right and Top-Left Diagonals
    for k in range(1, n):        
        if((row - k) < n and (col - k) < n and (row - k) >= 0 and (col - k) >= 0):
            if(board[row - k][col - k] == 1):       # Top-Left
                return False

    for k in range(1, n):    
        if((row - k) < n and (col + k) < n and (row - k) >= 0 and (col + k) >= 0):
            if(board[row - k][col + k] == 1):       # Top-Right
                return False
    
    return True


# Filling the Queens row-wise (one Queen at a time from Row 0 to Row n)
def n_queens(board, row):
    if(row == n):
        display(board)
        print("\n")
        return
    
    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1         # Place the Queen
            n_queens(board, row+1)      # Recursion
            board[row][col] = 0         # back-tracking    



board = [[0 for i in range(n)] for j in range(n)]
n_queens(board, 0)
