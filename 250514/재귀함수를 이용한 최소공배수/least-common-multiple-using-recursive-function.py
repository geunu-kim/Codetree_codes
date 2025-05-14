n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
tot = 1

def f(x,y) :
    global tot
    if x == 2 :
        if (tot * y[0]) % (y[1]) != 0 :
            tot *= y[0]
        if tot % y[1] != 0 :
            tot *= y[1]
    else :
        for i in range (x-1) :
            if i != (x-2) :
                if (tot * y[i]) % (y[i+1]) != 0 :
                    tot *= y[i]
                else :
                    continue
            else :
                if tot % y[i] != 0 :
                    tot *= y[i]
                else :
                    continue
    
    return tot

print(f(n,arr))