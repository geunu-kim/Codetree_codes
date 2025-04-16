n = 2
arr_2d = [
    list(map(int, input().split()))
    for _ in range (n)
]

for elem in arr_2d :
    a = sum(elem)
    b = (a/4)
    print(f"{b:.1f}", end=" ")
print()

c,d = 0,0
for i in range (4) :
    for j in range (2) :
        c += arr_2d[j][i]
        d = (c / 2)
    print(f"{d:.1f}", end=" ")
    c,d = 0,0
print()

e = 0
for elem in arr_2d :
    e += sum(elem)
f = (e/8)
print(f"{f:.1f}")