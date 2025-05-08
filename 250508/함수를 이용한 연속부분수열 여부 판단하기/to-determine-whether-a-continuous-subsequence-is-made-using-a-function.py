n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def part(x,y) :
    if x >= y :
        for i in range (x) :
            for n in range (y) :
                if a[i+n] == b[n] :      
                    if n == (y-1) :
                        return True
                    else :
                        continue
                else :
                    break
        return False
    else :
        return False


if part(n1,n2) :
    print("Yes")
else :
    print("No")