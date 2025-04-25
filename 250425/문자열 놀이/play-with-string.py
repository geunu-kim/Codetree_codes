S , Q = input().split()
P = list(S)

for i in range (int(Q)) :
    a = list(input().split())
    if a[0] == "1" :
        Z = int(a[1]) - 1 ; R = int(a[2]) - 1
        P[Z] , P[R] = P[R] , P[Z]
        V = ''.join(P)
        print(V)
    else :
        for j in range (len(P)) :
            if P[j] == str(a[1]) :
                P[j] = str(a[2])
        V = ''.join(P)
        print(V)


