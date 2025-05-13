n = int(input())

# Please write your code here.
def first(x) :
    if x == 0 :
        return
    
    first(x-1)
    print(x,end=" ")


def second(x) :
    if x == 0 :
        return

    print(x,end=" ")
    second(x-1)


first(n)
print()
second(n)