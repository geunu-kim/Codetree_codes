N = int(input())

# Please write your code here.
def f(x) :
    if x == 1 :
        return 1
    if x == 2 :
        return 2
    
    return f(x//3) + f(x-1)


print(f(N))