N = int(input())
a = 3 ; b = 6 ; c = 9

for _ in range (1, N+1) :
    if _ == a :
        print(0, end=" ")
        a += 10
    elif _ == b :
        print(0, end=" ")
        b += 10
    elif _ == c :
        print(0, end=" ")
        c += 10
    elif _ % 3 == 0 :
        print(0, end=" ")
    else :
        print(_, end=" ")
