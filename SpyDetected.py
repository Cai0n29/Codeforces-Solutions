t = int(input())
for i in range(t):
    a = int(input())
    n = input().split()
    least = min(n, key=n.count)
    print(int(n.index(least))+1)