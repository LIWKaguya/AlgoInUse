# Search x in arr, if it exists then return the location else -1
# Use this for sorted array

def binarySearch(arr, left, right, need):
    if right >= left:
        mid = left+(right-left)//2
        if arr[mid] == need:
            return mid
        if arr[mid] > need:
            return binarySearch(arr, left, mid-1, x)
        else:
            return binarySearch(arr, mid+1, right, x)
    else:
        return -1


l = [1, 3, 5, 19, 200]
x = 3
res = binarySearch(l, 0, len(l)-1, x)
if res != -1:
    print(f'Element exists at index {res+1}')
else:
    print(f'Element does not existed')

# Time complexity O(logn)
# Auxiliary space O(1)

# We use  [ mid = low + ( high - low ) // 2 ] because it may contain bug for overflow integer
# So the way [ mid = ( low + high ) // 2 ] is not bug-free 100%