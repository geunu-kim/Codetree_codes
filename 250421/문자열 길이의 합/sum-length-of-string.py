n = int(input())
cnt = 0 ; cnt_2 = 0
arr = []

for i in range (n) :
    a = input()
    cnt_2 += len(a)
    if a[0] == "a" :
        cnt += 1


print(cnt_2,cnt)


