N, M = map(int, input().split())

arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range (N)
]


arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range (N)
]


arr_2d_3 = [
    [0 for i in range (N)]
    for j in range (M)
]


for i in range (N) :
    for j in range (N) :
        if arr_2d_1[i][j] == arr_2d_2[i][j] :
            arr_2d_3[i][j] = 0
        else :
            arr_2d_3[i][j] = 1

for elem in arr_2d_3 :
    for elems in elem :
        print(elems, end=" ")
    print()
