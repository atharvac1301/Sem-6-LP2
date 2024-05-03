import heapq

def prims(graph, start):
    mst = []
    visited = []
    edges = [(cost, start, start) for neighbor, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.append(v)
            mst.append((u, v, cost))

            for neighbor, neighbor_cost in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (neighbor_cost, v, neighbor))

    return mst


def print_mst(mst):
    print("Edge\tWeight")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} \t {edge[2]}")


graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 5},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 5, 'D': 1}
}

start_node = 'A'
mst = prims(graph, start_node)
print_mst(mst)


