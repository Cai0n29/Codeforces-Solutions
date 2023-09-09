a, b = input().split()
b = int(b)
a = str(a)

for i in range(b):
    if str(a)[-1] == '0':
        a = str(a)[:-1]
    else:
        a = int(a) - 1
print(a)

