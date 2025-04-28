a , b = input().split()
c, d = 0 , 0

for i in range (len(a)) :
    if a[i].isdigit() == True :
        continue
    else :
        c = i
        break

for j in range (len(b)) :
    if b[j].isdigit() == True :
        continue
    else :
        d = j
        break

e = a[:c]
f = b[:d]

print(int(e) + int(f))