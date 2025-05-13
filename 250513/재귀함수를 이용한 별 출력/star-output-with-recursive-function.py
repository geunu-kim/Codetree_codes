n = int(input())

# Please write your code here.
def star(x) :
    if x == 0 :
        return

    star(x-1)
    print("*" * x)

star(n)