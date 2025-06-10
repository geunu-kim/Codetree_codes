n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0] * 1001

for i in range (len(segments)) :
    for j in range (segments[i][0] , segments[i][1]) :
        arr[j] += 1

max_arr = max(arr)
print(max_arr)