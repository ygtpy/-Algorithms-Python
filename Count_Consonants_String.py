
string1 = "abc def"
string2 = "yiGit ALi Sunal"
vowel = "aeiou"

def iterative_search(input_str):
    count=0 
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha(): 
            count += 1
    return count


print(iterative_search(string1))



#%%

def recursive_search(input_str):
    
    if input_str == '':
        return 0
    
    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1 + recursive_search(input_str[1:])
    else:
        return recursive_search(input_str[1:])


print(recursive_search(string1))        





