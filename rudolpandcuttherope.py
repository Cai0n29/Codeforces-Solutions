t = int(input())
for i in range(t):
    k = int(input())
    list = []
    diff =[]
    for x in range(k):
        a, b = input().split()
        a = int(a)
        b = int(b)
        sub = a-b
        list.append(sub)
    for p in list:
        if p > 0 and p != 0:
            diff.append(p)
    print(len(diff))
