M = int(input()) ; cnt = 0

for i in range (M) :
    a = int(input())
    while a != 1 :
        if a % 2 == 1 :
            a *= 3
            a += 1
            cnt += 1
        else :
            a /= 2
            cnt += 1
    print(cnt)
    cnt = 0


            