N = int(input())

# Please write your code here.
def total(x) :
    if x == 0 :
        return 0
    
    return total(x-1) + x


print(total(N))