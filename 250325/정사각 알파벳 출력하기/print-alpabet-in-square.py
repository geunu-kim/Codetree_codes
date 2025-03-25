n = int(input()) ; cnt = "A"

for i in range (n) :
    for j in range (n) :
        if j == n - 1 :
            print(cnt,end="")
            print()
            cnt = chr(ord(cnt) + 1)
        else :
            print(cnt,end="")
            cnt = chr(ord(cnt) + 1)





