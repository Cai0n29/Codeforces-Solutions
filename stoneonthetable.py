n = int(input())
word = input()
count =0
for i in range(n-1):
    if word[i] == word[i-1]:
        count+=1
print(count)