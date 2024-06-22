n = (int(input()))
all  = []
for i in range(100000+1): 
    if i%2 != 0:
        all.append(i)
app = []
ap = (n*n) % 10**6 + 37
for x in range(1, ap+1):
    a = all[:x]
    app.append(sum(a))
#print(sum(app)%1000037)
print(ap)


