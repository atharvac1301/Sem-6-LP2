
def display(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j] != None):
                print(state[i][j], end=" ")
            else:
                print(" ", end=' ')
        print()


class Node:
    def __init__(self, state=None, parent=None, move=None, h=0, g=0):
        self.state = state
        self.parent = parent
        self.h = h
        self.g = g
        self.move = move

    
class EightPuzzleProblem:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def solve(self):
        open_list = []
        closed_list = set()     # No duplicates

        start_node = Node(state=initial_state)
        open_list.append(start_node)
        
        while open_list:
            open_list.sort(key=lambda x: x.g + x.h)     # optional
            current_node = open_list.pop(0)
            closed_list.add(current_node)

            if(current_node.state == final_state):
                return self.trace_path(current_node)
            
            next_moves = self.get_possible_moves(current_node)

            for move, state in next_moves.items():
                child_node = Node(state, current_node, move, self.calc_h(state), current_node.g + 1)
                
                if child_node not in closed_list:
                    open_list.append(child_node)
                    

    def trace_path(self, node):
        path = []
        while node:
            path.append((node.move, node.state))
            node = node.parent

        return list(reversed(path))

    def get_possible_moves(self, node):
        possible_states = {}
        blank_row, blank_col = self.find_blank(node.state)

        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for row, col in moves:
            new_row = blank_row + row
            new_col = blank_col + col
            
            if(new_row >= 0 and new_row <= 2 and new_col >= 0 and new_col <= 2):
                new_state = [row[:] for row in node.state]      # create a copy of node.state
                new_state[blank_row][blank_col] = new_state[new_row][new_col]
                new_state[new_row][new_col] = None

                possible_states[(row, col)] = new_state     # key -> (row, col)  &  value -> (new_state)

        return possible_states
    
    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if(state[i][j] == None):
                    return i, j

    def calc_h(self, state):
        count = 0
        for i in range(3):
            for j in range(3):
                if(state[i][j] != self.final_state[i][j]):
                    count += 1
        return count


initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, None, 5]
]

final_state = [
    [1, 2, 3],
    [8, None, 4],
    [7, 6, 5]

]

move_name = {
    (1, 0)  : 'DOWN',
    (0, 1)  : 'RIGHT',
    (-1, 0) : 'UP',
    (0, -1) : 'LEFT',
    None : 'None'
    
}


solver = EightPuzzleProblem(initial_state, final_state)
solution_path = solver.solve()
print("Solution:")
for move, state in solution_path:
    print(move_name[move])
    display(state)
    print()

