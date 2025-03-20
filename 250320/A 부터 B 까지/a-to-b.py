S = input().split()
A = int(S[0]) ; B = int(S[1])

while A <= B :
    if A % 2 == 0 :
        print(A, end=" ")
        A += 3
    else :
        print(A, end=" ")
        A *= 2
    