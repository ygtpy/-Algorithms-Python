
s3 = "listen"
s4 = "slient"

s5 = "hello"
s6 = "world"

def anagram(word1, word2):
    
    char_count = {}
    
    if len(word1) != len(word2):
        return False
    
    for char in word1:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1

    for char in word2:
        if char in char_count:
            char_count[char] -=1
        else:
            return False
        
    for count in char_count.values():
        if count !=0:
            return False
        
    return True
   


print(anagram(s3, s4))
print(anagram(s5, s6))