n = int(input())

arr = [
    [0 for i in range (n)]
    for j in range (n)
]


num = 1

for i in range (n) :
    for j in range (n) :
        if i % 2 == 0 :
            arr[n-1-j][n-1-i] = num
            num += 1
        else :
            arr[j][n-1-i] = num
            num += 1

for elem in arr :
    for elems in elem :
        print(elems, end=" ")
    print()


