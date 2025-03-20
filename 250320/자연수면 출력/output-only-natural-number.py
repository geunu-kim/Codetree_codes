S = input().split()
A = int(S[0]) ; B = int(S[1])

if A >= 0 :
    for _ in range (B) :
        print(A, end="")
else :
    print(0)