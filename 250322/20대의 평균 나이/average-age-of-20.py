prod_1 = 0 ; prod_2 = 0

while True :
    a = int(input())
    if a < 30 :
        prod_1 += a
        prod_2 += 1
    else :
        ave = prod_1 / prod_2
        print(f"{ave:.2f}")
        break


