im = input().split()
im.sort()
inti = [int(x) for x in im]
len = 0
for i in inti:
    if i != max(inti) and i != min(inti):
       len = i
print((max(inti) - len) + (len - min(inti)))