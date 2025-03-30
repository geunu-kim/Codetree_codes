arr = list(map(int, input().split())) ; cnt = 0 ; sum_val = 0 ; average = 0

for i in range (10) :
    if arr[i] == 0 :
        break
    cnt += 1

for elem in arr[:cnt:] :
    sum_val += elem
    average = sum_val / cnt

print(f"{sum_val} {average:.1f}")