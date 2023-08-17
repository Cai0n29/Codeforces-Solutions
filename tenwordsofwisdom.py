t = int(input())
for i in range(t):
    all = 0
    ino = 0
    n = int(input())
    for h in range(n):
        a, b = map(int, input().split())
        if a<=10 and b>0:
          ino = b
          all = h
    print(int(all)+1)
       






        