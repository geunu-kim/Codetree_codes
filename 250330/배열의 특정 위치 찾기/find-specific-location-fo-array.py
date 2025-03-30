arr = list(map(int, input().split())) ; cnt = 0 ; arr_1, arr_2 = 0, 0

for i in range (1,len(arr) + 1,2) :
    arr_1 += arr[i]

for j in range (2,len(arr) + 1,3) :
    arr_2 += arr[j]
    cnt += 1

average = arr_2 / cnt

print(f"{arr_1} {average:.1f}")

