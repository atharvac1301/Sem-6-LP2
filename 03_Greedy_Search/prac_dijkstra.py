import heapq

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


graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}


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

start_node = 0
distances = dijkstra(graph, start_node)

print(f"Shortest distances from {start_node}")
for node, distance in distances.items():
    print(f"{node}  -  {distance}")


