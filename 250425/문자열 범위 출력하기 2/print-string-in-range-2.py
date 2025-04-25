a = input()
b = int(input())

if len(a) >= b :
    for i in range (b) :
        print(a[len(a)-1-i],end="")
else :
    for i in range (len(a)) :
        print(a[len(a)-1-i],end="")

