N = int(input())

# Please write your code here.
def double (x) :
    if (x) < 10 :
        return (x ** 2)
    
    return double(x // 10) + ((x % 10) ** 2)


print(double(N))