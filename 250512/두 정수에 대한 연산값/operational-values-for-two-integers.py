a, b = map(int, input().split())

# Please write your code here.


def calculate (x,y) :
    if x > y  :
        x += 25
        y *= 2
    elif x < y :
        y += 25
        x *= 2
    return x , y

a,b = calculate(a,b)

print(a,b)