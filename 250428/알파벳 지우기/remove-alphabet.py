a = input()
b = input()

c = []
d = []

for i in range (len(a)) :
    if a[i].isdigit() == True :
        c.append(a[i])
    else :
        continue

for j in range (len(b)) :
    if b[j].isdigit() == True :
        d.append(b[j])
    else :
        continue

e = ''.join(c)
f = ''.join(d)

print(int(e) + int(f))


