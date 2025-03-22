n = int(input())

P = "N"
for _ in range (2,n) :
    if n % _ == 0 :
        P = "C"
        break
    else :
        continue

print(P)

