prod = 0

while True :
    a = int(input())
    if a % 2 == 0 :
        print(int(a / 2))
        prod += 1
        if prod == 3 :
            break
    else :
        continue


        