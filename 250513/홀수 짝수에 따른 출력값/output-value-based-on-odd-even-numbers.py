N = int(input())

# Please write your code here.
def f(x) :
    if x == 2 :
        return 2
    if x == 1 :
        return 1
    
    return f(x-2) + (x)


print(f(N))