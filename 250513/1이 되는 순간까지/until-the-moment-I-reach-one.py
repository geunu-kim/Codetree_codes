N = int(input())

# Please write your code here.
tot = 0

def f(x) :
    global tot
    if x % 2 == 0 :
        x /= 2
        tot += 1
        if x == 1 :
            return tot
        return f(x)
    else :
        x //= 3
        tot += 1
        if x == 1 :
            return tot
        return f(x)


print(f(N))