N = int(input())
prod = 0

while True :
    if N == 1 :
        print(prod)
        break  
    elif N % 2 == 0 :
        N /= 2
        prod += 1
    elif N % 2 == 1 :
        N *= 3
        N += 1
        prod += 1
    
