k = int(input())
for i in range(k):
    l = input()
    if (l[0] == 'Y' or l[0] == 'y') and (l[1] == 'E' or l[1] == 'e') and (l[2] == 'S' or l[2] == 's'):
        print("YES")
    else:
        print("NO")
