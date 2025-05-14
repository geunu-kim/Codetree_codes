n = int(input())

# Please write your code here.
cnt = 0

def f(x) :
    global cnt
    
    while x != 1 :
        if x % 2 == 0 :
            x //= 2
            cnt += 1
        else :
            x *= 3
            x += 1
            cnt += 1

    return cnt


print(f(n))