
def is_palindrome(string):
    
    string = string.replace(" "," ")
    string = string.lower()
    d = dict()
    
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
     
    odd_count = 0        
    for k, v in d.items():
        if v % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palindrome(palin_perm))  
print(is_palindrome(not_palin_perm))  


























