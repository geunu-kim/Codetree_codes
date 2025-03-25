for i in range (1,20) :
    for n in range (1,20) :
        print(f"{i} * {n} = {i*n}", end="")
        if n == 19 :
            print()
        elif  n % 2 == 1:
            print(" / ",end="")
        else :
            print()

            
