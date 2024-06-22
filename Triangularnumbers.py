n = int(input())
all =[]
for i in range(500):
    all.append(i)
app =[]
for x in range(500):
    a = all[:x]
    app.append(sum(a))
if n in app:
    print('YES')
else:
    print('NO')