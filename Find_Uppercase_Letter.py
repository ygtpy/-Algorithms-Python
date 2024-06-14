
str1 = "Yigit Ali"
str2 = "yigit Ali"
str3 = "yigit ali"


def find_iterative(input_str):
    
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character"


def find_recursive(input_str, indx=0):
    
    if input_str[indx].isupper():
        return input_str[indx]
    if indx == len(input_str) - 1:
        return "No Upercase Character"
    return find_recursive(input_str, indx + 1)



print(find_iterative(str1))
print(find_iterative(str2))
print(find_iterative(str3))


#%%

print(find_recursive(str1))
print(find_recursive(str2))
print(find_recursive(str3))













































































