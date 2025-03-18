A = input().split()
Aa = int(A[0])
Ab = str(A[1])

B = input().split()
Ba = int(B[0])
Bb = str(B[1])

if (Aa >= 19 and Ab == "M") or (Ba >= 19 and Bb == "M") :
    print("1")
else :
    print("0")