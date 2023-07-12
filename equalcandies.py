import math
p = int(input())
for i in range(p):
    num = int(input())
    lis = input().split()
    p = [int(x) for x in lis]
    nonmini = []
    insum = []
    mini = min(p)
    k = [int(x) for x in lis]
    for nu in lis:
        if nu != mini:
            nonmini.append(nu)
        z = [int(x)-mini for x in nonmini]
        Sum = sum(z)
    print(Sum)
    
        
        
        
    