S = input().split()
A = str(S[0]) ; N = int(S[1])
a = 1

if A == "A" :
    for _ in range (N) :
        print(a, end=" ")
        a += 1
elif A == "D" :
    for _ in range (N) :
        print(N, end=" ")
        N -= 1