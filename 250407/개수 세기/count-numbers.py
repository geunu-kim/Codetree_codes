arr = list(map(int, input().split()))
N = arr[0] ; M = arr[1]

arr_2 = list(map(int, input().split()))
cnt = 0

for i in range (N) :
    if arr_2[i] == M :
        cnt += 1
    else :
        pass

print(cnt)

