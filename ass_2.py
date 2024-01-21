# A* Algorithm

heuristic_values = {
    'S' : 13,
    'A' : 12,
    'B' : 4,
    'C' : 7,
    'D' : 3,
    'E' : 8,
    'F' : 2,
    'H' : 4,
    'I' : 9,
    'G' : 0
}

def heuristic(state):
    return heuristic_values[state]

graph = {
    'S' : [['A', 3], ['B', 2]],
    'A' : [['C', 4], ['D', 1]],
    'B' : [['E', 3], ['F', 1]],
    'E' : [['H', 5]],
    'F' : [['I', 2], ['G', 3]],
    'G' : [['G', 0]]
    
}


def a_star(graph):
    shortest_path = ['S']
    path_length = 0
    temp = 'S'

    while temp != 'G':
        min_fvalue = 9999
        best_state = None
        current_path_value = 0
        g = 0
        for state in graph[temp]:
            g = state[1]
            h = heuristic(state[0])
            f = g + h
            if f < min_fvalue:
                min_fvalue = f
                best_state = state[0]
                current_path_value = state[1]
        
        temp = best_state
        shortest_path.append(best_state)
        path_length += current_path_value
    
    return shortest_path, path_length


shortest_path, path_length = a_star(graph)

print(shortest_path)
print(path_length)



    
    













