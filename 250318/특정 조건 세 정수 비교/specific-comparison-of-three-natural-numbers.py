D = input().split()

a = int(D[0])
b = int(D[1])
c = int(D[2])

if a <= b and a <= c :
    if a == b and a == c :
        print("1 1")
    else :
        print("1 0")
else :
    print("0 0")