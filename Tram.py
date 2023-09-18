n = int(input())
k =0
all =[]
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0:
        k = k + b
    else:
        k = k+b -a
    all.append(k)
print(max(all))
