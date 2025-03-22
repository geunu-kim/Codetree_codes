N = int(input())
prod = 0

while True :
    if N % 2 == 0 :
        prod += 1
        N /= 2
    else :
        print(prod)
        break

