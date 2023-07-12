def all(o):
    if o % 2== 0:
        return o/2
    else:
        ine = (o-1) / 2
        return ine - o
p = int(input())
print (int(all(p)))




