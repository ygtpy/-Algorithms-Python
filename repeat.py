import random
veri = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
hedef = random.randint(1, 37)

def linear_search(veri, hedef):

    for i in range(len(veri)):
        if veri[i] == hedef:
            return True 
    return False  


print(linear_search(veri, hedef))



#%%

# Iterative Binary Search
veri = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
hedef = random.randint(1, 37)

def  iterative(veri, hedef):
    low = 0
    high = len(veri) - 1
    
    while low <= high:
        mid = (low + high) //2
        if hedef == veri[mid]:
            return mid
        elif hedef < veri[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

sonucIterative = iterative(veri, hedef)
if sonucIterative != False:
    print(f"Veri {sonucIterative} indexinde bulundu")
else:
    print("Veri Bulunamadı")
#%% Recursive Binary Search

veri = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
hedef = random.randint(1, 37)

def recursive(veri, hedef, low, high):
    
    if low > high:
        return False
    
    mid = (low + high) //2

    if hedef == veri[mid]:
        return mid
    elif hedef < veri[mid]:
        return recursive(veri, hedef, low, mid - 1)
    else:
        return recursive(veri, hedef, mid + 1, high)


sonucRecursive = recursive(veri, hedef, 0, len(veri)-1)

if sonucRecursive != False:
    print(f"Veri {sonucRecursive} indexinde bulundu")
else:
    print(f"Veri {sonucRecursive} indexinde bulundu")




#%%


string1="yigit ali sunal"
unsuz="aeiou"

def iterative_search(cumle):
    count = 0
    for i in range(len(cumle)):
        if cumle[i].lower() not in unsuz and cumle[i].isalpha():
            count += 1
    return count

print(iterative_search(string1))



#%%

def recurdive_search(cumle):

    if cumle == '':
        return 0
    
    if cumle[0].lower() not in unsuz and cumle[0].isalpha():
        return 1+ recurdive_search(cumle[1:])
    return recurdive_search(cumle[1:])


print(recurdive_search(string1))




#%%

import random 

x = random.randint(0, 20)
y = random.randint(0, 20)

def recursive_multiply(x, y):
    
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

print(f"x: {x}, y: {y}")
print(recursive_multiply(x, y))








































































