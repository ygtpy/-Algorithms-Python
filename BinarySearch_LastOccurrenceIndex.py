


def find(A, target):
    low = 0
    high = len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] == target:

            if mid == len(A) - 1 or A[mid + 1] != target:
                return mid
            else:
                low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 285
x = find(A, target)
print(x) 










