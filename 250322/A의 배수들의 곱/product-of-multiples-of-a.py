arr = input().split()
a = int(arr[0]) ; b = int(arr[1]) ; prod = 1

for _ in range (1,b+1) :
    if _ % a == 0 :
        prod *= _

print(prod)

