n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0] * 9999
for start , end in segments :
    for j in (start , end) :
        arr[j] += 1

max_arr = max(arr)
print(max_arr)