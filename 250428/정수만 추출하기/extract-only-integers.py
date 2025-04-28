a , b = input().split()
c, d = 0 , 0

for i in range (len(a)) :
    if a[i].isdigit() == False :
        c = i
        break
    elif i == (len(a) - 1) :
        a[i].isdigit() == True
        c = i + 1
        break
    else :
        continue
        
for j in range (len(b)) :
    if b[j].isdigit() == False :
        d = j
        break
    elif j == (len(b) - 1) :
        b[j].isdigit() == True
        d = j + 1
        break
    else :
        continue

e = a[:c]
f = b[:d]

print(int(e) + int(f))