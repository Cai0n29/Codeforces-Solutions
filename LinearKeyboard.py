n = int(input())
for i in range(n):
    alph = input()
    word = input()
    all =[]
    for i in word:
        all.append(alph.find(i)+1)
    up= []
    for i in range(len(all)-1):
        up.append(abs((all[i-(len(all)-1)])- all[i]))
    print(sum(up))