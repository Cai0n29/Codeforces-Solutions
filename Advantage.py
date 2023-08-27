t = int(input())
for i in range(t):
    k = int(input())
    n = input().split()
    n =[int(x) for x in n]
    m = [int(x) for x in n]
    m.sort()
    maxi = max(n)
    sec = m[-2]
    list =[]
    for y in n:
        if y != maxi:
            y = y - maxi
            list.append(y)
        else:
            y = y - sec
            list.append(y)
    print(str(list).replace('[','').replace(',','').replace(']',''))
            
    