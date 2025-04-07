n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
b = []
c = a[0]

for i in range (n) :
    if c <= a[i] :
        c = a[i]

a.remove(c)

d = a[0]

for i in range (n-1) :
    if d <= a[i] :
        d = a[i]

print(c,d)