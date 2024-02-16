
graph1 = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

graph2 = [
    [0, 1, 9, 0, 0, 0],
    [1, 0, 8, 2, 7, 0],
    [9, 8, 0, 3, 0, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 0, 4, 0, 5],
    [0, 0, 0, 6, 5, 0]
]

def primsMST(graph):
    n = len(graph)
    result = []
    visited = [False] * n
    pq = []             # Priority Queue Stores vertices and weight (of the edge)
    mst_weight = 0      # Total Weight of the MST

    pq.append([0, 0, 0])    # vertex 1, vertex 2, weight

    while pq:
        vertex1, vertex2, weight = pq.pop()
        if visited[vertex1]:
            continue
        
        result.append([(vertex1, vertex2), weight])
        mst_weight += weight
        visited[vertex1] = True

        for i in range(n):          
            if(graph[vertex1][i] != 0 and (not visited[i])):
                pq.append([i, vertex1, graph[vertex1][i]])
                pq.sort(key=lambda x : x[-1], reverse=True)
                
    return result, mst_weight

result, mst_weight = primsMST(graph1)
result.pop(0)       # 0 - 0 edge is not required in MST

print("Edge\tWeight")
for res in result:
    print(f"{res[0][0]} - {res[0][1]}     {res[1]}")

print(f"\n\nWeight of the MST is {mst_weight}")






















