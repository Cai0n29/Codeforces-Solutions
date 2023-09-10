n = int(input())
k = str(n+1)
count = 0
while k[0] == k[1] or k[1] == k[2] or k[2] ==k[3] or k[1] == k[3] or k[0] == k[3] or k[0] == k[2]:
    k = str(int(k) +1)
print(k)