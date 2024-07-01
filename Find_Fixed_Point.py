
def Binary_Search(A):
    
    low = 0
    high = len(A)- 1 
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid -1
        else:
            return A[mid]
    return None


A = [-10, -5, 0, 3, 7]
print(Binary_Search(A))

#%%

def Linear_Search(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


A = [-10, -5, 0, 3, 7]
print(Linear_Search(A))


#%%

def function_option(A):
    for index, value in enumerate(A):
        if index == value:
            return value
    return None
    

A = [-10, -5, 9, 3, 7]
print(function_option(A))


#%%

def function_choice(liste):
    result = next(filter(lambda x: x[0] == x[1], enumerate(liste)), None)
    return result[1] if result else None

A = [-10, -5, 9, 3, 7]
print(function_choice(A))












