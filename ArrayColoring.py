n = int(input())
for i in range(n):
    a = int(input())
    lis = input().split()
    lis = [int(x) for x in lis]
    all = sum(lis)
    if all % 2== 0:
        print('YES')
    else:
        print('NO')