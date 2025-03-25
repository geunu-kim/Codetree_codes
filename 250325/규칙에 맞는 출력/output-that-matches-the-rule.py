N = int(input())

for i in range (N) :
    c = N - i
    for j in range (i+1) :
        print(c,"",end="")
        c += 1
    print()
