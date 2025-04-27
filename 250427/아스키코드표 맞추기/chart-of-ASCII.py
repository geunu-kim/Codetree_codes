a = list(map(int, input().split()))

b = [
    chr(a[i])
    for i in range(len(a)) 
]

for elem in b :
    print(elem, end= " ")