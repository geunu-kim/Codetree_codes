n = int(input())

# Please write your code here.

def ques(x) :
    if x % 2 == 0 and ((x // 10) + (x % 10)) % 5 == 0  :
        print("Yes")
    else :
        print("No")

ques(n)

