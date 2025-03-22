N = int(input())

P = "C"
for _ in range (2,N) :
    if N % _ == 0 :
        break
    else :
        P = "P"
        break
print(P)