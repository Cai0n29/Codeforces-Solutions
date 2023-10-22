n = int(input())

for i in range(n):
    p = int(input())
    ap = input()
    up = input()
    all = []
    ull =[]
    for i in ap:
        if i == 'B':
            all.append('G')
        else:
            all.append(i)
    for i in up:
        if i == 'B':
            ull.append('G')
        else:
            ull.append(i)
    if str(all).replace('[', '').replace(']','').replace(',','').replace(' ','').replace("'",'') == str(ull).replace('[', '').replace(']','').replace(',','').replace(' ','').replace("'",''):
        print('YES')
    else:
        print('NO')
  
            
    