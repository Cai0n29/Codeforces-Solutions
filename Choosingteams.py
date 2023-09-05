n, k = input().split()
n = int(n)
k = int(k)
all = input().split()
all = [int(x) for x in all]
count = 0
for i in all:
    if i+k <= 5:
        count+=1 
print(count//3)