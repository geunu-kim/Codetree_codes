n = int(input())

for i in range (1,n+1) :
    for j in range (1,n+1) :
        if n - i + 1 >= j :
            print(f"{i} * {j} = {i*j}", end="")
            if n - i + 1 != j :
                print(" / ", end="")
            else :
                print()
        else :
            pass

