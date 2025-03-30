arr = list(map(int, input().split())) ; cnt = 0 ; sum_val = 0 ; cnt_2 = 0 ; average = 0


for i in range (10) :
    if arr[i] == 0 :
        break
    cnt += 1

for elem in arr[:cnt:] :
    if elem % 2 == 0 :
        sum_val += elem
        cnt_2 += 1
    else :
        pass

print(f"{cnt_2} {sum_val}")

