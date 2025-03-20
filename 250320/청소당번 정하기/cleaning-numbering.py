n = int(input())
cnt_1 = 0 ; cnt_2 = 0 ; cnt_3 = 0

for _ in range (1,n+1) :
    if _ % 12 == 0 :
        cnt_3 += 1
    elif _ % 6 == 0 :
        cnt_2 += 1
    elif _ % 3 == 0 :
        cnt_2 += 1
    elif _ % 2 == 0 :
        cnt_1 += 1

print(cnt_1,cnt_2,cnt_3)