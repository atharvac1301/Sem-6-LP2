
# n = int(input("Enter the number of Vertices: "))
# e = int(input("Enter the number of Edges: "))

graph = {
    0 : [1, 2, 3],
    1 : [0, 2],
    2 : [0, 1, 4],
    3 : [0],
    4 : [2]
    
}

n = len(graph)      
e = 0

for i in range(0, n):
    e += len(graph[i])

e = int(e/2)

def bfs(graph, n, e):
    queue = [0]
    traversed_list = []

    while(len(queue) != 0):
        temp = queue.pop(0)
        if temp not in traversed_list:
            traversed_list.append(temp)
            for i in graph[temp]:
                queue.append(i)
    
    print("BFS Traversal:", traversed_list)

def dfs(graph, n, e):
    stack = [0]
    traversed_list = []

    while(len(stack) != 0):
        temp = stack.pop(-1)
        if temp not in traversed_list:
            traversed_list.append(temp)
            for i in reversed(graph[temp]):
                stack.append(i)
    
    print("DFS Traversal:", traversed_list)

dfs(graph, n, e)






























