
def normalize(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()


def unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

def unique_2(input_str):
    return len(set(input_str)) == len(input_str)


def unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

print(unique_1(normalize(unique_str)))
print(unique_1(normalize(non_unique_str)))

print(unique_2(normalize(unique_str)))
print(unique_2(normalize(non_unique_str)))

print(unique_3(normalize(unique_str)))
print(unique_3(normalize(non_unique_str)))






























