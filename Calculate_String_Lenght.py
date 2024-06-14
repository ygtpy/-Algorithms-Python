input_str = "yigit ali"

print(len(input_str))

def iterative_len(input_str):
    
    count = 0
    for i in range(len(input_str)):
        if input_str[i] != ' ':
            count +=1
    return count


def recursive_len(input_str):
    if input_str == '':
        return 0
    elif input_str[0] == ' ':
        return recursive_len(input_str[1:])
    else:
        return 1 + recursive_len(input_str[1:])



print(iterative_len(input_str))
print(recursive_len(input_str))




