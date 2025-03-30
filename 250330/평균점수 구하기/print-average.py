arr = list(map(float, input().split()))
cnt = len(arr) ; sum_val = 0 ; average = 0

for elem in arr :
    sum_val += elem

average = float(sum_val / cnt)

print(f"{average:.1f}")

