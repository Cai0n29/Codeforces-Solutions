n5, n6, n7, n8 =input().split()
n1 = int(n5)
n2 = int(n6)
n3 = int(n7)
n4 = int(n8)
p = [n1, n2, n3, n4]
maxi = max(p)
mini = []
ning=[]
for i in p:
    if i!= maxi:
        mini.append(i)
mini =[abs(item - maxi) for item in mini]

[print(i, end =' ') for i in mini]
