n = input()
all = 0
up = ''
while all < len(n):
    if n[all] == '.':
        up+='0'
        all+=1
    elif n[all] == '-' and n[all+1] == '.':
        up+='1'
        all+=2
    else:
        up+='2'
        all+=2
print(up)