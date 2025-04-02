arr = list(map(int , input().split()))
new_arr = [0] * (arr[1]) ; cnt = 0

while True :
    new_arr[arr[0] % arr[1]] += 1
    arr[0] //= arr[1]
    if arr[0] <= 1 :
        break

for elem in new_arr :
    cnt += (elem ** 2)

print(cnt)

