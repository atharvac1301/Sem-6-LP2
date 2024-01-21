# N-Queen Problem

global n
n = 4


def display(board):
    n = len(board)
    for i in range(n):
        print(board[i])


def isSafe(board, row, col):

    for k in range(n):
        if(board[k][col] == 1):
            return False
    for k in range(n):
        if(board[row][k] == 1):
            return False
    
    for k in range(1, n):
        if((row + k) < n and (col + k) < n and (row + k) >= 0 and (col + k) >= 0):
            if(board[row + k][col + k] == 1):
                return False
    
    for k in range(1, n):        
        if((row - k) < n and (col - k) < n and (row - k) >= 0 and (col - k) >= 0):
            if(board[row - k][col - k] == 1):
                return False
    
    for k in range(1, n):
        if((row + k) < n and (col - k) < n and (row + k) >= 0 and (col - k) >= 0):
            if(board[row + k][col - k] == 1):
                return False

    for k in range(1, n):    
        if((row - k) < n and (col + k) < n and (row - k) >= 0 and (col + k) >= 0):
            if(board[row - k][col + k] == 1):
                return False
        
    return True

# def isSafe2(board, row, col):

#     # check only the same row as n_queens() will fill a Queen for each column --> column by column
#     for j in range(n):          
#         if(board[row][j] == 1):                                               
#             return False    
    
#     for i, j in range(row, -1), range()

    
#     pass


def n_queens(board, col):
    if(col == n):
        display(board)
        print("\n")
        return
    
    for row in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1       # Place the Queen
            
            n_queens(board, col+1)      # Recursion
            
            board[row][col] = 0       # back-tracking
    


board = [[0 for i in range(n)] for j in range(n)]

n_queens(board, 0)
