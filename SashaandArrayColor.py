import math 
p = int(input())
for i in range(p):
    a, b = input().split()
    a = int(a)
    b = int(b)
    po = pow(a, b) 
    ten = pow(10, 9)
    print(po % (ten + 7))