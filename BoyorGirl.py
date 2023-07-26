word = input()

leng = len(dict.fromkeys(word))
if leng%2 == 0:
    print("CHAT WITH HER!")
else: 
    print("IGNORE HIM!")