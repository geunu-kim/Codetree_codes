N = int(input())
prod = 0

for _ in range (1,N+1) :
    if _ % 2 == 0 or _ % 3 == 0 or _ % 5 == 0 : 
        continue
    else :
        prod += 1

print(prod)

