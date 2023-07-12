p = int(input())
for i in range(p):
    first = int(input())
    word = input()
    li = []
    for char in word:
        if char == 'a':
            li.append(1)
        elif char == 'b':
            li.append(2)
        elif char == 'c':
            li.append(3)
        elif char == 'd':
            li.append(4)
        elif char == 'e':
            li.append(5)
        elif char == 'f':
            li.append(6)
        elif char == 'g':
            li.append(7)
        elif char == 'h':
            li.append(8)
        elif char == 'i':
            li.append(9)
        elif char == 'j':
            li.append(10)
        elif char == 'k':
            li.append(11)
        elif char == 'l':
            li.append(12)
        elif char == 'm':
            li.append(13)
        elif char == 'n':
            li.append(14)
        elif char == 'o':
            li.append(15)
        elif char == 'p':
            li.append(16)
        elif char == 'q':
            li.append(17)
        elif char == 'r':
            li.append(18)
        elif char == 's':
            li.append(19)
        elif char == 't':
            li.append(20)
        elif char == 'u':
            li.append(21)
        elif char == 'v':
            li.append(22)
        elif char == 'w':
            li.append(23)
        elif char == 'x':
            li.append(24)
        elif char == 'y':
            li.append(25)
        elif char == 'z':
            li.append(26)
    print(max(li))
            
    