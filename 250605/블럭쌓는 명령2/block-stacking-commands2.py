n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
arr = [0 for i in range (n)]
# Please write your code here.
for start , end in commands :
    if end == n :
        for i in range (start , end) :
            arr[i] += 1

    for i in range (start , end + 1) :
        arr[i] += 1


print(max(arr))