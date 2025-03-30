arr = list(map(int, input().split())) ; cnt = 0 ; sum_val = 0

for elem in arr :
    if elem == 0 :
        break
    cnt += 1

if cnt == 3 :
    for elem in arr[cnt-1::-1] :
        sum_val += elem
else :
    for elem in arr[cnt-1:cnt-4:-1] :
        sum_val += elem

print(sum_val)

