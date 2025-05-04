n = int(input())

# Please write your code here.

def ques(x) :
    if x % 2 == 0 and x[0] + x[1] % 5 == 0 :
        print("Yes")
    else :
        print("No")

ques(n)

