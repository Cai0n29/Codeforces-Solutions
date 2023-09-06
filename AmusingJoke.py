a = input()
b = input()
c = input()

count =0
if sorted(a+b) == sorted(c):
    print('YES')
else:
    print('NO')