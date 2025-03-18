A = input().split()

a = int(A[0])
b = int(A[1])

if a < b :
    print('1 0')
else :
    if a == b :
        print('0 1')
    else :
        print('0 0')