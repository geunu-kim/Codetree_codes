N = int(input()) ; cnt = 0 ; cnt_2 = 0

for i in range (N) :
    arr = input().split() ; a = int(arr[0]) ; b = int(arr[1])
    for j in range (a,b+1) :
        if j % 2 == 0 :
            cnt += j
    print(cnt)
    cnt = 0
    


