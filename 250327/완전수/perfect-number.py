start, end = map(int, input().split())

# Please write your code here.
cnt_1 , cnt_2 = 0 , 0

for i in range (start, end+1) :
    for j in range (1,i) :
        if i % j == 0 :
            cnt_1 += j
    if  cnt_1 == i :
        cnt_2 += 1
        cnt_1 == 0
        if i == end :
            print(cnt_2)
    else :
        cnt_1 == 0
        if i == end :
            print(cnt_2)
