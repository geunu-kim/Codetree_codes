arr = input().split()
a = int(arr[0]) ; b = int(arr[1]) ; prod = 1

for _ in range (a, b+1) :
    prod *= _

print(prod)