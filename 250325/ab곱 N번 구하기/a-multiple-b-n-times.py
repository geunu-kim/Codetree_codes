n = int(input()) ; c = 1

for i in range (n) :
    arr_1 = input().split() ; a = int(arr_1[0]) ; b = int(arr_1[1])
    for j in range (b-a+1) :
        c *= b
        b -= 1
        if b == a - 1 :
            pass
    print(c)
    c = 1







