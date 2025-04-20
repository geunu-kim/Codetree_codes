n = int(input()) 

arr = [
    [1] * (i+1)
    for i in range (n)
]

if n >= 3 :
    for i in range (2,n) :
        for j in range (1,i) :
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for elem in arr :
    for elems in elem :
        print(elems, end=" ")
    print()


