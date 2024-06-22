n = int(input())
for i in range(n):
    p = int(input())
    lis = input()
    dupli = len(lis) - len(set(lis))
    all = len(set(lis)) * 2
    print(dupli + all)