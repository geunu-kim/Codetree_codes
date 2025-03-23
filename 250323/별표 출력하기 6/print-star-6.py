N = int(input())

for i in range (N) :
    for j in range (i*2) :
        print("","",end="")
    for j in range (2*N-1-2*i) :
        print("*","",end="")
    for j in range (i*2) :
        print("","",end="")
    print()

for i in range (N-1) :
    for j in range (2*N-2*i-4) :
        print("","",end="")
    for j in range (2*i+3) :
        print("*","",end="")
    for j in range (2*N-2*i-4) :
        print("","",end="")
    print()

