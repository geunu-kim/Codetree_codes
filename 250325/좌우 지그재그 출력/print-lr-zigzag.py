n = int(input()) ; cnt = 1

for i in range (n) :
    for j in range (n) :
        if i % 2 == 0 :
            print(cnt,"",end="")
            cnt += 1
        elif j == n-1 :
            print(cnt+n-j-1,"",end="")
            cnt += n
        else :
            print(cnt+n-j-1,"",end="")
    print()


