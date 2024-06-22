import random

x = random.randint(0, 20)
y = random.randint(0, 20)

def recursive_multiply(x,y):
    
    if x < y :
        return recursive_multiply(y, x)
    
    if y == 0:
        return 0 
    return x + recursive_multiply(x, y-1)


print(f"x: {x}, y: {y}")
print(recursive_multiply(x, y))

