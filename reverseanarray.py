n = int(input())
k = input().split()
k.reverse()
k = [int(x) for x in k]
print(str(k).replace('[', '').replace(',','').replace(']',''))