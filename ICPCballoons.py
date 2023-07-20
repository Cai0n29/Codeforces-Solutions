n = int(input())
add = 0
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    if (b-a) >= 2:
        add+=1
print(add)


