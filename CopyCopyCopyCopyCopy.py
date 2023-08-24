n = int(input())
for i in range(n):
    p = int(input())
    list = input().split()
    inti = [int(x) for x in list]
    inti.sort()
    a = len(set(inti))
    print(a)
