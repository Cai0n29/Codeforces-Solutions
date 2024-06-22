#add 1 to the minimum value in the list 
#My Solution
#sort the list and add 1 to the smallest or ap[0]
n = int(input())
for i in range(n):
    p = int(input())
    ap = input().split()
    ap.sort()
    ap[0] = int(ap[0]) + 1
    all  = [int(x) for x in ap]
    v = 1
    for i in all:
        v = v*i
    print(v)