v = int(input())
a = int(input())
r = int(input())
p = int(input())
h = int(input())
if  ((v+a+r)>=h) and ((v+a+h)>=h) and ((a+r+p)>=h) and ((r+p+v))>=h:
    print('WAW')
else:
    print('AWW')