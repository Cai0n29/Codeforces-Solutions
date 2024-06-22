
t = int(input())
for i in range(t):
    a, b, c = input().split()
    isita = 0
    isitb = 0
    isitc = 0
    if a != b and a != c:
        isita = 1
    elif b !=a and b != c:
        isitb = 1
    elif c != a and c !=b:
        isitc = 1
    if isita == 1:
        print(a)
    elif isitb == 1:
        print(b)
    else:
        print(c)
        
