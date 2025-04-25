n = int(input())
a = []

for i in range (n) :
    b = input()
    a.append(b)

c = ''.join(elem for elem in a)

print(c)

