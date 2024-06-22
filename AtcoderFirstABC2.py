n = int(input())
word = input()
if word.find('ABC') == 0 and word != 'ABC':
    print(-1)
else:
    print(word.find('ABC') +1)