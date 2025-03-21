sum_val = 0 ; ave_val_1 = 0 ; cnt = 0

for _ in range (10) :
    a = int(input())
    if a >= 0 and a <= 200 :
        sum_val += a
        ave_val_1 += a 
        cnt += 1

ave_val_2 = ave_val_1 / cnt

print(f"{sum_val} {ave_val_2:.1f}")

