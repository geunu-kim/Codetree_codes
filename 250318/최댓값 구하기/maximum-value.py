A = input().split()

a = int(A[0])
b = int(A[1])
c = int(A[2])

if (a >= b and b >= c) or (a >= c and a >= b) :
    print(a)
elif (b >= a and a >= c) or (b >= c and c >= a) :
    print(b)
else :
    print(c)