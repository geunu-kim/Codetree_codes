n = 4

arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

for _ in range (n) :
    print(sum(arr_2d[_]))

