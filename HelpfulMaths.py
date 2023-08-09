n = input()
lists = []
for vals in n:
    if vals != '+':
        lists.append(vals)
intlist = [int(x) for x in lists]
intlist.sort()
print(str(intlist).replace('[', '').replace(']', '').replace(', ', '+'))
