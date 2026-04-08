def soma(*args):
    total = 0
    for num in args:
        total+=num
    return total

print(soma(2,3,4,6,2,4555,2343,23,34,333))