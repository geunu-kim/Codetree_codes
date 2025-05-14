N = int(input())

# Please write your code here.
def f(x) :
    if x == 1 :
        return 2
    if x == 2 :
        return 4
    
    return ((f(x-1) * f(x-2)) % 100)
    

print(f(N))