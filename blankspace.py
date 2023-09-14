n = int(input())
for i in range(n):
    k = int(input())
    l = input().split()
    x = [int(x) for x in l]
    c = 0
    up = 0
    max_count =0
    list = []
    for j in x:
        if j == 0:
            c += 1
            max_count = c
        else:
            if c > max_count:
                max_count = c
           
            c = 0
        list.append(max_count)
    print(max(list))


  

    
    
