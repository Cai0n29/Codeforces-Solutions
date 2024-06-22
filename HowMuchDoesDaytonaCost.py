n = int(input())
for i in range(n):
    a, b= input().split()
    a = int(a)
    b = int(b)
    lis = input().split()
    lis = [int(x) for x in lis]
    if b in lis:
        print('YES')
    else:
        print('NO')