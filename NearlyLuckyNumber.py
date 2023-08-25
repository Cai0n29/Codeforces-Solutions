n = input()
four = 0
sev =0

for i in (n):
    if i == '4':
        four +=1
    elif i == '7':
        sev+=1

if (sev + four == 7) or (sev + four == 4):
    print('YES')
else:
    print('NO')