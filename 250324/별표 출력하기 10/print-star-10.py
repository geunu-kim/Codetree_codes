N = int(input())

for i in range (2*N) :
    if (i+1) % 2 == 1 :
        for j in range ((i+1)//2 + 1) :
            print("* ",end="")
        print()
    else :
        for j in range (N+1-(i+1)//2) :
            print("* ",end="")
        print()

