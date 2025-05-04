n = int(input())

# Please write your code here.

def add(n) :
    tot = 0
    for i in range (1,n+1) :
        tot += i
    tot_2 = tot // 10
    return tot_2

a = add(n)
print(a)