n, m = map(int, input().split())

# Please write your code here.

arr_2d = [
    [0 for i in range (m)]
    for j in range (n)
]

num = 0

for i in range (m) :
    for j in range (n) :
        if i % 2 == 0 :
            arr_2d[j][i] = num
            num += 1
        else :
            arr_2d[n-j-1][i] = num
            num += 1

for elem in arr_2d :
    for elems in elem :
        print(elems, end=" ")
    print()

