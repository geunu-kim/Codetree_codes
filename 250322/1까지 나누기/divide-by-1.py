N = int(input())
prod = 0 ; prod_2 = 0

for _ in range (1, 5000) :
    N //= _
    prod += 1
    if N <= 1 :
        print(prod)
        break


