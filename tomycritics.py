p = int(input())
for i in range(p):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if ((a+b) >= 10)  or ((b+c) >= 10) or ((a+c) >= 10):
        print("YES")
    else:
        print("NO")