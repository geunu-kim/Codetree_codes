a, b, c = map(int, input().split())

# Please write your code here.
tot = 0

def f(x,y,z) :
    global tot
    q = x * y * z
    while True :
        tot += (q % 10)
        q //= 10
        if q < 10 :
            tot += q
            break
    return tot


print(f(a,b,c))