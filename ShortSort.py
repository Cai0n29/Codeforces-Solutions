n = int(input())
for i in range(n):
    app = input()
    if app == 'abc' or app == 'acb' or app == 'bac' or app == 'cba':
        print('YES')
    else:
        print('NO')