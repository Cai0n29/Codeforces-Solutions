n = int(input())
for i in range(n):
    m = int(input())
    all = []
    for x in range(1, 10000+1):
        if str(x)[-1] != '3' and x % 3 != 0:
            all.append(x)
    print(all[m-1])
