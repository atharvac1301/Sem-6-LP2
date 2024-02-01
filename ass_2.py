
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


def display(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] != None):
                print(board[i][j], end = " ")
            else:
                print('-', end = " ")

        print()


def h_value(current_state, final_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != final_state[i][j]:
                count += 1
    return count

def blank_row_col(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j] == None):
                return i, j


def a_star(blank_row, blank_col, current_state, final_state):
    move_row = [1, 0, -1, 0]
    move_col = [0, 1, 0, -1]

    if(current_state == final_state):
        return current_state

    possible_states = []
    h_values = []
    for i in range(4):
        temp_state = current_state
        temp_row = blank_row + move_row[i]
        temp_col = blank_col + move_col[i]
        if(temp_row >= 0 and temp_row <= 2 and temp_col >= 0 and temp_col <= 2):

            temp_state[blank_row][blank_col] = temp_state[temp_row][temp_col]
            temp_state[temp_row][temp_col] = None
            possible_states.append(temp_state)
            
    
    min_h = 9999
    min_hindex = -1
    for i in range(len(possible_states)):
        h = h_value(possible_states[i], final_state)
        if(h < min_h):
            min_h = h
            min_hindex = i
        h_values.append(h)
        
    best_state = possible_states[min_hindex]
    blank_row, blank_col = blank_row_col(best_state)

    return a_star(blank_row, blank_col, best_state, final_state)


state = a_star(2, 1, initial_state, final_state)

display(state)









