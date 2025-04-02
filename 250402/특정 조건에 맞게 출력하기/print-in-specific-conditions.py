N = list(map(int, input().split()))
arr = []

for elem in N :
    if elem == 0 :
        break
    elif elem % 2 == 1 :
        arr.append(elem + 3)
    else :
        arr.append(elem // 2)

for elem in arr :
    print(elem, end=" ")



