n = int(input())
for i in range(n):
    all = input()
    div = (len(all)//2)
    if len(all) % 2 == 0 and all[:div] == all[div:]:
        print('YES')
    else:
        print('NO')