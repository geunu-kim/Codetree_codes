a = input()

b = list(a)

c = b[1]

d = b[0]

for i in range (len(b)) :
    if b[i] == c :
        b[i] = d

f = ''.join(b)

print(f)

