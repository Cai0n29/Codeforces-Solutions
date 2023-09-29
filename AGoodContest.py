n = int(input())
all =[]
for i in range(n):
    name, bef, aft = input().split()
    bef = int(bef)
    aft = int(aft)
    if bef >= 2400 and aft>bef:
        all.append('YES')
if all == []:
    print('NO')
else:
    print('YES')