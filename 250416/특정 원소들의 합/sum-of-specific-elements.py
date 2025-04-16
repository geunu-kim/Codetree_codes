n = 4
arr_2d = [
    list(map(int, input().split()))
    for i in range (4)
]

arr = []

for i in range (4) :
    for j in range (4) :
        if i >= j :
            arr.append(arr_2d[i][j])

b = sum(arr)
print(b)