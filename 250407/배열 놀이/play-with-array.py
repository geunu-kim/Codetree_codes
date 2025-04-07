arr = list(map(int, input().split()))
N = arr[0] ; Q = arr[1]

arr_2 = list(map(int, input().split()))
idx = 1

for i in range (Q) :
    a = list(map(int, input().split()))
    if a[0] == 1 :
        print(arr_2[a[1] - 1])
    elif a[0] == 2 :
        for elem in arr_2 :
            if elem == a[1] :
                break
            else :
                idx += 1
        if a[1] in arr_2 :
            print(idx)
        else :
            print(0)
        idx = 1
    else :
        s = a[1] ; e = a[2]
        for i in range (s-1,e) :
            print(arr_2[i], end=" ")
        print()
    
            