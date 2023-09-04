n = int(input())
for i in range(n):
    at =[]
    for x in range(8):
        dot = input()
        for all in dot:
            if all != '.':
                at.append(all)
    print(str(at).replace('[', '').replace("'",'').replace(",", '').replace(']','').replace(' ', ''))