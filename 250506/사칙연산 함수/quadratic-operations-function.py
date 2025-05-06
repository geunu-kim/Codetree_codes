a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def plus(x, y) :
    return (x + y)

def minus(x, y) :
    return (x - y)

def divide(x, y) :
    return (x // y)

def double(x, y) :
    return (x * y)


if o == "+" :
    print(a, "+", c, "=", plus(a,c))
elif o == "-" :
    print(a, "-", c, "=", minus(a,c))
elif o == "/" :
    print(a, "/", c, "=", divide(a,c))
elif o == "*" :
    print(a, "*", c, "=", double(a,c))
else :
    print("False")