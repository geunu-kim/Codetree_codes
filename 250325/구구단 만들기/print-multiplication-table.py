arr = input().split() ; a = int(arr[0]) ; b = int(arr[1])
c = (b//2) - (a//2) + 1

for i in range (1,10) :
    for j in range (c) :
        print(f"{b-2*j} * {i} = {(b-2*j)*i}",end="")
        if j != c-1 :
            print(" / ",end="")
        else :
            print()

