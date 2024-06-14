import random
data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = random.randint(0, 40)

# Linear Search 
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

print(linear_search(data, target))
#%%
# Iterative Binary search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else: 
            low = mid + 1
    return False        

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = random.randint(0, 40)

result = binary_search_iterative(data, target)
if result != False:
    print(f"Hedef {result} indeksinde bulundu.")
else:
    print("Hedef dizide bulunamadı.")


#%%
# Binary Search Recursive
def binary_search_recursive(data, target, low, high):
    
    if low > high:
        return False
    
    mid = (low + high) // 2
    
    if target == data[mid]:
        return mid
    
    elif target < data[mid]:
        return binary_search_recursive(data, target, low, mid - 1)
    
    else:
        return binary_search_recursive(data, target, mid + 1, high)



data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = random.randint(0, 40)


result = binary_search_recursive(data, target, 0, len(data) - 1)


if result != False:
    print(f"Hedef {result} indeksinde bulundu.")
else:
    print("Hedef dizide bulunamadı.")


#%%






















































































