n, m = map(int, input().split())

# Please write your code here.

def method(x,y) :
    num = 2 ; cnt = 0
    if x <= y :
        while True :
            if (num * x) % y == 0 :
                cnt = (num * x)
                break
            else :
                num += 1
    else :
        while True :
            if (num * y) % x == 0 :
                cnt = (num * y)
                break
            else :
                num += 1
    print(cnt)


method(n,m)