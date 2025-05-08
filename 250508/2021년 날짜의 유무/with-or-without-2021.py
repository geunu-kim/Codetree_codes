M, D = map(int, input().split())

# Please write your code here.

def date(x,y) :
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12 :
        if y >= 1 and y <= 31 :
            return True
        else :
            return False
    elif x == 2 :
        if y >= 1 and y <= 28 :
            return True
        else :
            return False
    elif x == 4 or x == 6 or x == 9 or x == 11 :
        if y >= 1 and y <= 30 :
            return True
        else :
            return False
    else :
        return False



if date(M,D) :
    print("Yes")
else :
    print("No")