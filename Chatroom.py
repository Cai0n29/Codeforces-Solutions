import re
x = input()

if re.match(r'.*?h[^e]*e[^l]*l[^l]*l[^o]*o',x):
    print ('YES')
else:
    print('NO')