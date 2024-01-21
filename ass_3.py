# Selection Sort

arr = [8,89,4,2,6,3,10,]

def swap(a, b):
    a, b = b, a


def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    
    return arr

print(arr)
arr = selection_sort(arr)
print(arr)




