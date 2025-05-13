n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(x,y) :
    for i in range (x-1) :
        if y[i] < y[i+1] :
            continue
        else :
            y[i] , y[i+1] = y[i+1] , y[i]
    return y[x-1]

print(f(n,arr))