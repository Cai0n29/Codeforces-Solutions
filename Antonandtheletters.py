letters= input().replace(',', '').replace(' ', '').replace('{','').replace('}','')
list =[]
for i in  letters:
    list.append(i)

if letters != '{}':
    all = set(list)
    print(len(all))
else:
    print(0)

