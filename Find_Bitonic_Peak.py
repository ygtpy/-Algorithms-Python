

def find_Bitonic_Peak(arr):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]
  
        elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            low = mid + 1

        else:
            high = mid - 1

arr = [1, 3, 8, 12, 4, 2]
print(find_Bitonic_Peak(arr))


#%%


