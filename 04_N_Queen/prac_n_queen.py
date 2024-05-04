global n 
n = 4

board = [[0 for i in range(n)] for i in range(n)]


def display(board):
    for row in board:
        print(row)
    print("\n\n")

def isSafe(board, row, col):

    for k in range(n):
        if board[k][col] == 1:
            return False
    
    for k in range(1, n):
        











