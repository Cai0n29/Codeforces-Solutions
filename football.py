l = input()
x = [int(x) for x in l]
c = 0
up = 0
max_count =0
list = []

ones = 0
op = 0
all =[]
for j in x:
    if j == 0:
        c += 1
        max_count = c
    else:
        if c > max_count:
            max_count = c
        c = 0
    list.append(max_count)
ones = 0
op = 0
all =[]
for j in x:
    if j == 1:
        ones+=1
        op = ones
    else:
        if ones> op:
            op = ones
        ones = 0
    all.append(ones)
if max(list) >=7 or max(all) >= 7:
    print('YES')
else:
    print('NO')