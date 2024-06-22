n = input().lower().replace(' ','')
if n[-2] == 'a' or n[-2] == 'e' or n[-1] =='i' or n[-2] =='o' or n[-2] =='u' or n[-2] =='y':
    print('YES')
else:
    print('NO')
            