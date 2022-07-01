# Search x in arr, if it exists then return the location else -1

def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


l, num = [1, 2, 3, 4, 5, 6], 4
length = len(l)
res = search(l, length, num)
if res == -1:
    print('Element does not exists')
else:
    print(f'Element exists in index {res+1}')

# Time complexity O(n)
# Auxiliary space O(1)
