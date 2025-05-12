n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def hehe(x) :
    tot = 0
    global m
    while m != 0 :
        if m % 2 == 0 :
            tot += x[m-1]
            m //= 2
        else :
            tot += x[m-1]
            m -= 1
    return tot


print(hehe(A))

