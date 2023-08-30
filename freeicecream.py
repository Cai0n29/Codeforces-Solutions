a, b = input().split()
a = int(a)
b = int(b)
count = 0
for _ in range(a):
    sym, num = input().split()
    num = int(num)
    if sym == '+':
        b = b + num 
    elif sym == '-' and b >= num:
        b = b - num
    elif b< num:
        count +=1
print(b, count)