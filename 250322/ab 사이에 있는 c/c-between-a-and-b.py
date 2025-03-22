arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
P = 0

for _ in range (a, b+1) :
    if _ % c == 0 :
        P = 'YES'
        break
    else :
        P = 'NO'
        continue

print(P)