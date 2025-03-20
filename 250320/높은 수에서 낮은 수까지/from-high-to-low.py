S = input().split()
A = int(S[0]) ; B = int(S[1])

if A > B :
    for _ in range (A, B-1, -1) :
        print(A, end= " ")
        A -= 1
elif A < B :
    for _ in range (B, A-1, -1) :
        print(B, end=" ")
        B -= 1
else :
    print(A)