n, m = map(int, input().split())

# Please write your code here.

arr = [
    [0 for i in range (m)]
    for j in range (n)
]

num = 1 ; a = 0 ; cnt = 1 ; b = 0 ; cnt_2 = 1

for i in range (m) :
    arr[a][i] = num
    num += 1
    if a != i and a <= 2 :
        while a != i and a <= 2 and (a + 1) <= (n - 1):
            arr[a + 1][i - (1 * cnt)] = num
            a += 1
            cnt += 1
            num += 1
        a = 0
        cnt = 1
    if i == (m-1) :
        while b + cnt_2 <= (n-1) :
            arr[b + cnt_2][m - 1 - b] = num
            num += 1
            b += 1
            if b + cnt_2 == n :
                cnt_2 += 1
                b = 0

for elem in arr :
    for elems in elem :
        print(elems, end=" ")
    print()