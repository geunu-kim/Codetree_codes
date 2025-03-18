D = input().split()

a = int(D[0])
b = int(D[1])
c = int(D[2])

if a<=b and a<=c :
    print(a)
elif b<=a and b<=c :
    print(b)
elif c<=a and c<=b :
    print(c)