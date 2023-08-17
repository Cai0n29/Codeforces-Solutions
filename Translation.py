n = input()
opp = input()
if n[::-1] == opp:
    print("YES")
else:
    print("NO")

#Another solution
def hello(k):
    k = k[::-1]
    return k

k = input()
a = input()
if hello(k) == a:
    print("YES")
else:
    print("NO")