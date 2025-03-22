arr = input().split()
a = int(arr[0]) ; b = int(arr[1])

P=0
for _ in range (a,b+1) :
    if 1920 % _ == 0 and 2880 % _ == 0 :
        P = 1
        break
    else :
        continue

print(P)

