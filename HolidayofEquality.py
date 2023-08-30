n = int(input())
list = input().split()
list = [int(x) for x in list]
maxi = max(list)
all = []
for i in list:
    i = maxi - i
    all.append(i)
print(sum(all))   