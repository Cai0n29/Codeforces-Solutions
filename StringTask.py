n = input().lower()
all = []
for i in n:
    if i != 'a' and i !='e' and i !='i' and i !='o' and i!='u' and i!='y':
        all.append(i)
all = str(all).replace('[','').replace(']','').replace(',','').replace("'",'')
print('.' + str(all).replace(' ','.'))