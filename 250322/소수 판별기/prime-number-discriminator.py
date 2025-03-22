N = int(input())
P = 0

for _ in range (2,N) :
    if N % _ == 0 :
        P = "C"
        break
    else :
        P = "P"
        continue
        
print(P)