N, M = map(int, input().split())
num = 1

arr_2d = [
    [0 for i in range (M)]
    for j in range (N)
]

for i in range (N) :
    for j in range (M) :
        arr_2d[i][j] = num
        num += 1

for elem in arr_2d :
    for elem_2 in elem :
        print(elem_2, end=" ")
    print()
