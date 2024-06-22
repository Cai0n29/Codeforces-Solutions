n = int(input())
a = input().split()
s = int(input())
b = input().split()
present =0
notin = 0
absent =0
for i in a:
    if i in b:
        present+=1
    elif i not in b:
        absent+=1
for x in b:
    if x not in a:
        notin+=1
print(present)
print(absent)
print(notin)