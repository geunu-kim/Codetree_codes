n = int(input())

for i in range (n) :
    if i == 0 :
        for j in range (n) :
            print("* ",end="")
        print()
    else :
        for j in range (n) :
            if j % 2 == 0 :
                print("  ",end="")
            else: 
                if i <= j :
                    print("* ",end="")
                else :
                    print("  ",end="")
        print()




