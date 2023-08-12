n = int(input())
x = 0
for i in range(n):
    l = input()
    if l == '++X' or l == 'X++':
        x = x + 1
    elif l == '--X' or l == 'X--':
        x = x - 1
    print(x)
    