n = int(input())
a = input().split()
b = input().split()
count = 0
all = set(a[1:]+b[1:])
all = [int(x) for x in all]
all.sort()
list =[]
for i in range(1,n+1):
    list.append(i)
if list == all:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')