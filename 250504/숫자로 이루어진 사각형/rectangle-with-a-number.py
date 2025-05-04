n = int(input())

# Please write your code here.
def square (x) :
    num = 1
    for i in range (x) :
        for j in range (x) :
            print(num, end=" ")
            num += 1
            if num == 10 :
                num = 1
        print()


square(n)

