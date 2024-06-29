

def perm_1(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    
    if len(str1) != len(str2):
        return False
    
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    
    
    n = len(str1)
    for i in range(n):
        if str1[i] != str2[i]:
            return False
    return True
   

print(perm_1("God", "dog"))  
print(perm_1("Not", "top"))

#%% faster solution

def perm_2(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count ={}
    for char in str1:
        char_count[char] = char_count.get(char,0)+1
            
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False
            
    return all(count == 0 for count in char_count.values())

print(perm_2("God", "dog"))
print(perm_2("Not", "top"))
print(perm_2("abcdefghijklmnopqrstuvwxyz" * 100, "zyxwvutsrqponmlkjihgfedcba" * 100))





