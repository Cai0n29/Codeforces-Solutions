n = int(input())
pang = input().lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 0
#check if the character in pang is all in alphabet 
for char in alphabet:
    if char not in pang:
        count+=1 
if count >0 :
    print('NO')
else:
    print('YES')

