arr = input().split() ; a = int(arr[0]) ; b = int(arr[1])
c = b - a + 1

for i in range (1,5) :
    for j in range (c) :
        print(f"{b} * {2*i} = {b*(2*i)}",end="")
        b -= 1
        if j != c-1 :
            print(" / ",end="")
        else :
            print()
    b += c

