n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absolute(x) :
    if x < 0 :
        x2 = x
        x += (-x)
        x += (-x2)
    return x


for elem in arr :
    elem = absolute(elem)
    print(elem, end=" ")

