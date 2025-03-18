L = input().split()

A, B, C = int(L[0]), int(L[1]), int(L[2])

if (A>B and C>A) or (B>A and A>C) :
    print(A)
elif (A>B and B>C) or (C>B and B>A) :
    print(B)
else :
    print(C)