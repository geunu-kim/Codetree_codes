a = input() ; b = []

for i in range (len(a)) :
    if i % 2 == 1 :
        b.append(a[i])
    else :
        continue

b.reverse()

c = ''.join(elem for elem in b)

print(c)