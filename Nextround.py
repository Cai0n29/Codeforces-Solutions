a, b = input().split()
a = int(a)
b = int(b)
list = input().split()
list = [int(x) for x in list]
list.insert(0, 0)
count =0
for i in list:
    if i >= list[b] and i > 0:
        count+=1
print(count)
    