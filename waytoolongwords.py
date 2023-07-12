k = int(input())
for i in range(k):
    s = input()
    mij = len(s) -2
  
    org = len(s)
    if org <= 10:
        print(s)
    else:
        print(s[0] + str(mij) + s[-1])