N = int(input())

for i in range (N-1) :
    for j in range (i+1) :
        print("*",end="")
    print()
    print()

for i in range (N) :
    print("*",end="")
print()
print()

for i in range (N-1) :
    for j in range (N-i-1) :
        print("*",end="")
    print()
    print()

