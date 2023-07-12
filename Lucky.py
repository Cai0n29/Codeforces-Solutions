p = int(input())
for i in range(p):
    k = input()
    l = int(k[1]) + int(k[0]) + int(k[2])
    o = int(k[3]) + int(k[4]) + int(k[5])
    if l == o:
        print("YES")
    else:
        print("NO")
        