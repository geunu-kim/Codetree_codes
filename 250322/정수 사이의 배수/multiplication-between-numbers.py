arr = input().split()
a = int(arr[0]) ; b = int(arr[1])
sum_val = 0 ; ave_val_1 = 0 ; cnt = 0

for _ in range (a, b+1) :
    if _ % 5 == 0 or _ % 7 == 0 :
        sum_val += _
        ave_val_1 += _
        cnt += 1

ave_val_2 = ave_val_1 / cnt

print(f"{sum_val} {ave_val_2:.1f}")