N = int(input()) ; cnt = 65

for i in range (N) :
    for j in range (i+1) :
        if j != i :
            print(chr(cnt),end="")
            cnt += 1
            if cnt == 91 :
                cnt = 65
        else :
            print(chr(cnt),end="")
            print()
            cnt += 1
            if cnt == 91 :
                cnt = 65
