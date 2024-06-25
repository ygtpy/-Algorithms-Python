
def spread_column(column_str):
    
    num = 0
    count = len(column_str) -1
    for s in column_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num



print(spread_column("A"))
print(spread_column("Z"))
print(spread_column("ADD"))





