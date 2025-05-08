n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def re_double(_list) :
    for i in range (n) :
        if _list[i] % 2 == 0 :
            _list[i] /= 2
            _list[i] = int(_list[i])
        else :
            continue


re_double(arr)

for elem in arr :
    print(elem, end=" ")
