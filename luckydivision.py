n = input()
count = 0
all = str(set(n)).replace("'",'').replace(',','').replace('{', '').replace('}','').replace(' ', '')
if all == '47' or all =='74' or int(n)%4==0 or int(n)%7 ==0:
    print('YES')
else:
    print('NO')