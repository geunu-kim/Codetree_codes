A = input().split()
aM = int(A[0])
aE = int(A[1])

B = input().split()
bM = int(B[0])
bE = int(B[1])

if aM > bM :
    print("A")
elif aM == bM :
    if aE > bE :
        print("A")
    elif aE < bE :
        print("B")
else :
    print("B")