a = input() ; b = list(a)

c = b[0] ; d = b[1]

for i in range (len(b)) :
    if b[i] == c :
        b[i] = d
    elif b[i] == d :
        b[i] = c

e = ''.join(b)

print(e)