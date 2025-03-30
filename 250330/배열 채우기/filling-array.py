arr = list(map(int, input().split()))

if arr[-1] == 0 :
    for elem in arr[-2::-1] :
        print(elem,end=" ")
else :
    for elem in arr[::-1] :
        print(elem,end=" ")


