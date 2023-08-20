
n = int(input())
for i in range(n):
    p = int(input())
    list = input().split()
    n = [int(x) for x in list]
    n.sort()
    t =''
    if all(i<j for i, j in zip(n, n[1:])):
        t='YES'
    else:
        t = 'NO'
    print(t)
    