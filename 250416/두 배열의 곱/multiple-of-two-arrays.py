arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range (3)
]

a = input()

arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range (3)
]

arr_2d_3 = [
    [0 for i in range (3)]
    for j in range (3)
]

for i in range (3) :
    for j in range (3) :
        arr_2d_3[i][j] = (arr_2d_1[i][j] * arr_2d_2[i][j])

for elem in arr_2d_3 :
    for elem_2 in elem :
        print(elem_2, end=" ")
    print()


