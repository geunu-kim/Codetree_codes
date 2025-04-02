arr = [0] * 5

for i in range (3) :
    a = list(input().split())
    if str(a[0]) == "Y" and int(a[1]) >= 37 :
        arr[1] += 1
    elif str(a[0]) == "N" and int(a[1]) >= 37 :
        arr[2] += 1
    elif str(a[0]) == "Y" and int(a[1]) < 37 :
        arr[3] += 1
    else :
        arr[4] += 1

for i in range (4) :
    print(arr[i+1], end=" ")

if arr[1] >= 2 :
    print("E", end="")