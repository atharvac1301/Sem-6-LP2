matrix = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0],
            
        ]


def isSafe(matrix, i, j, visited):
    m = len(matrix)
    n = len(matrix[0])

    return i >= 0 and i < m and j >= 0 and j < n and matrix[i][j] and (not visited[i][j])

# Neighbors' (row, col) values
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(matrix, visited, sx, sy):

    q = []
    q.append([sx, sy])
    visited[sx][sy] = True

    while q:
        temp = q.pop(0)
        x, y = temp[0], temp[1]

        for i in range(8):
            if isSafe(matrix, x + row[i], y + col[i], visited):
                q.append([x + row[i], y + col[i]])
                visited[x + row[i]][y + col[i]] = True



def DFS(matrix, visited, x, y):

    visited[x][y] = True

    for i in range(8):
        if isSafe(matrix, x + row[i], y + col[i], visited):
            DFS(matrix, visited, x + row[i], y + col[i])



def countIslandsBFS(matrix):
    m = len(matrix)
    n = len(matrix[0])

    visited = [[False for i in range(n)] for i in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] and (not visited[i][j]):
                BFS(matrix, visited, i, j)
                count += 1

    return count

def countIslandsDFS(matrix):
    m = len(matrix)
    n = len(matrix[0])

    visited = [[False for i in range(n)] for i in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] and (not visited[i][j]):
                DFS(matrix, visited, i, j)
                count += 1

    return count


print(countIslandsBFS(matrix))
print(countIslandsDFS(matrix))







