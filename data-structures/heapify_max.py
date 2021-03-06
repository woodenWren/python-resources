def heapify_helper(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify_helper(arr, n, largest)
        
def heapify(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify_helper(arr, n, i)
        
        
        
# Finally, to print the heap in order:
for i in range(len(arr)):
    arr[0], arr[-1] = arr[-1], arr[0]
    print(arr.pop())
    heapify_helper(arr, len(arr), 0)
