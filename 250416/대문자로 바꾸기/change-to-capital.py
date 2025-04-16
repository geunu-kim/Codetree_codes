n = 5

arr_2d = [
    list(map(str, input().split()))
    for _ in range (n)
]

for elem in arr_2d :
    for _ in elem :
        print(_.upper(), end=" ")
    print()
