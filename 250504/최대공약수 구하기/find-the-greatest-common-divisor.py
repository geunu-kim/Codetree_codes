n, m = map(int, input().split())

# Please write your code here.

def GCD(x,y) :
    num = 0
    if x >= y :
        for i in range (1,y+1,1) :
            if y % i == 0 and x % i == 0 :
                num = i
    else :
        for i in range (1,x+1,1) :
            if x % i == 0 and y % i == 0 :
                num = i
    print(num)


GCD(n,m)