N = int(input()) ; cnt = 0 ; cnt_2 = 0

for i in range (2,N+1) :
    for j in range (1,i+1) :
        if i % j == 0 :
            cnt += 1
    if cnt == 2 :
        print(i,"",end="")
        cnt = 0
    else :
        cnt = 0
