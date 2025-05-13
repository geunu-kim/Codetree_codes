n = int(input())

# Please write your code here.
def stars_2 (x) :
    if x == 0 :
        return
    
    print("* "* x)
    stars_2 (x-1)
    print("* "* x)


stars_2(n)