N = int(input())

# Please write your code here.
def flower (x) :
    if x == 0 :
        return
    
    print(x,end=" ")
    flower(x-1)
    print(x,end=" ")


flower(N)