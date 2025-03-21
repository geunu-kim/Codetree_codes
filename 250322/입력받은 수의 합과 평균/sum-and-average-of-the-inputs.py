N = int(input()) ; sum_val = 0 ; ave_val = 0 ; cnt = 0

for _ in range (N) :
    a = int(input())
    sum_val += a
    ave_val += a
    cnt += 1

ave_val_2 = ave_val / cnt

print(f"{sum_val} {ave_val_2:.1f}")
