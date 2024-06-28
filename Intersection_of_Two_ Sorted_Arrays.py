
def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []
    
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
                
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
            
        else: # A[i] > B[j] 
            j += 1
            
    return intersection


A = [1, 2, 3, 4, 5, 5, 3, 7]
B = [1, 4, 2, 7, 3, 5, 5, 4, 2]
A.sort()
B.sort()

print(intersect_sorted_array(A, B))






