N = int(input())

# Please write your code here.
def f(x) :
    if x == 1 :
        return 1

    return f(x-1) * (x)


print(f(N))