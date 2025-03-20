cnt_1 = 0
cnt_2 = 0
a = 0
for _ in range (10) :
    a = int(input())
    if a % 3 == 0 and a % 5 == 0 :
        cnt_1 += 1
        cnt_2 += 1
    elif a % 3 == 0 :
        cnt_1 += 1
    elif a % 5 == 0 :
        cnt_2 += 1

print(cnt_1,cnt_2)
    