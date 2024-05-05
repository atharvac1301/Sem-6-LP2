"""
Count the Number of Islands Problem
0 - Water, 1 - Land
Neighboring 1's form an Island 

"""

matrix = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0],
            
        ]


# To check if the cell at (i, j) can be included in the island or not
def isSafe(matrix, i, j, visited):
    m, n = len(matrix), len(matrix[0])

    return i >= 0 and i < m and j >= 0 and j < n and matrix[i][j] and (not visited[i][j])
        

# add this to get the coordinates of the neighbours
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(matrix, visited, sx, sy):

    q = []
    q.append([sx, sy])
    visited[sx][sy] = True

    while(len(q) > 0):
        temp = q.pop(0)

        x, y = temp[0], temp[1]

        for k in range(8):
            if isSafe(matrix, x + row[k], y + col[k], visited):
                visited[x + row[k]][y + col[k]] = True
                q.append([x + row[k], y + col[k]])


def DFS(matrix, visited, x, y):

    visited[x][y] = True

    for k in range(8):
        if isSafe(matrix, x + row[k], y + col[k], visited):
            DFS(matrix, visited, x + row[k], y + col[k])
    

def countIslandBFS(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[0 for i in range(n)] for i in range(m)]

    count = 0

    for i in range(m):
        for j in range(n):
            if(matrix[i][j] and not visited[i][j]):
                BFS(matrix, visited, i, j)
                count += 1

    return count

def countIslandDFS(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[0 for i in range(n)] for i in range(m)]

    count = 0

    for i in range(m):
        for j in range(n):
            if(matrix[i][j] and not visited[i][j]):
                DFS(matrix, visited, i, j)
                count += 1

    return count

print(countIslandDFS(matrix))
print(countIslandBFS(matrix))














