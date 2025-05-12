a, b = map(int, input().split())

# Please write your code here.
def balance(x,y) :
    if x > y :
        x *= 2
        y += 10
        return x,y
    else :
        y *= 2
        x += 10
        return x,y


a,b = balance(a,b)
print(a,b)