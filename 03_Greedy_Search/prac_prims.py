import heapq


"""
graph = {
    0 : {1 : 4, 7 : 8},
    1 : {0 : 4, 2 : 8, 7 : 11},
    2 : {1 : 8, 3 : 7, 5 : 4, 8 : 2},
    3 : {2 : 7, 4 : 9, 5 : 14},
    4 : {3 : 9, 5 : 10},
    5 : {2 : 4, 3 : 14, 4 : 10, 6 : 2},
    6 : {5 : 2, 7 : 1, 8 : 6},
    7 : {0 : 8, 1 : 11, 6 : 1, 8 : 7},
    8 : {2 : 2, 6 : 6, 7 : 7}

}

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
    edges = [(cost, start, neighbor) for neighbor, cost in graph[start].items()]

    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.append(v)
            mst.append((u, v, cost))
            for neighbor, neighbor_cost in graph[v].items():
                heapq.heappush(edges, (neighbor_cost, v, neighbor))
    
    return mst

def print_mst(mst):
    print("Edge \t Weight")
    temp = []
    for edge in mst:
        if (edge[1], edge[0]) not in temp:
            print(f"{edge[0]} - {edge[1]} \t {edge[2]}")
            temp.append((edge[0], edge[1]))


start_node = 'A'
mst = prims(graph, start_node)
print_mst(mst)



