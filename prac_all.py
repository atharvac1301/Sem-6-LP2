import heapq

"""Count Number of Islands DFS and BFS
"""

matrix = [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    
]

m = len(matrix)
n = len(matrix[0])

def isSafe(matrix, x, y, visited):
    return x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] and (not visited[x][y])

row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

def BFS(matrix, visited, sx, sy):
    q = []
    q.append([sx, sy])
    visited[sx][sy] = True

    while q:
        x, y = q.pop(0)

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
    visited = [[False for j in range(n)] for i in range(m)]

    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] and not visited[i][j]:
                BFS(matrix, visited, i, j)
                count += 1
    return count

def countIslandsDFS(matrix):
    visited = [[False for j in range(n)] for i in range(m)]

    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] and not visited[i][j]:
                DFS(matrix, visited, i, j)
                count += 1
    return count

# print(countIslandsBFS(matrix))
# print(countIslandsDFS(matrix))


"""
Prims Algo for Minimum Spanning Tree
"""

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 5},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 5, 'D': 1}
}


def prims(graph, start):
    mst = []
    visited = []
    pq = [(cost, start, neighbor) for neighbor, cost in graph[start].items()]

    heapq.heapify(pq)

    while pq:
        cost, u, v = heapq.heappop(pq)

        if v not in visited:
            visited.append(v)
            mst.append((u, v, cost))
            for neighbor, neighbor_cost in graph[v].items():
                heapq.heappush(pq, (neighbor_cost, v, neighbor))

    return mst

def print_mst(mst):
    print("Edge\t Weight")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]}\t {edge[2]}")


# start_node = 'A'
# mst = prims(graph, start_node)
# print_mst(mst)


"""
Dijkstra's Algo for Single Source Shortest Path
"""

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}



def dijkstra(graph, start):
    distances = {node:9999 for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if distances[current_node] < current_dist:
            continue

        for neighbor, neighbor_weight in graph[current_node].items():
            neighbor_dist = current_dist + neighbor_weight
            
            if neighbor_dist < distances[neighbor]:
                distances[neighbor] = neighbor_dist
                heapq.heappush(pq, (neighbor_dist, neighbor))

    return distances

start = 'A'
distances = dijkstra(graph, start)
# print("Node\tDistance")
# for node, dist in distances.items():
#     print(f"{node}\t{dist}")


n = 4

board = [[0 for i in range(n)] for j in range(n)]

def print_board(board):
    for row in board:
        print(row)
    print("\n")

def isSafe(board, row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for k in range(n):
        if all(0 <= x < n for x in [row-k, col-k]):
            if board[row-k][col-k] == 1:
                return False

        if all(0 <= x < n for x in [row-k, col+k]):
            if board[row-k][col+k] == 1:
                return False

    return True

def n_queen(board, row):
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1
            n_queen(board, row+1)
            board[row][col] = 0
    

# n_queen(board, 0)








