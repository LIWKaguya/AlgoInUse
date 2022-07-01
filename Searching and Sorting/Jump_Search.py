# Search x in arr, if it exists then return the location else -1
# Use this for sorted array
import math

def jumpSearch(arr, x, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1

l = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
need = 55
length = len(l)

ind = jumpSearch(l, need, length)
if ind == -1:
    print('The element does not exist')
else:
    print(f'The element is presented at index {ind+1}')

# Time complexity O(√n)
# Auxiliary space O(1)

# Binary search is better but the Jump search only traverse back once.
# In situation that the binary search is costly then Jump search can be used
