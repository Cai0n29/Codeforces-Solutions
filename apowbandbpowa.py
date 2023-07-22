import math
a, b = input().split()
a = int(a)
b = int(b)
apow = pow(a, b)
bpow = pow(b, a)
print(apow-bpow)
