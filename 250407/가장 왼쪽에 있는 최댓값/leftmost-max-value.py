n = int(input())
a = list(map(int, input().split()))

while True :
    b = max(a)
    c = a.index(b)
    print(c+1,end=" ")
    if c==0 :
        break
    a = a[:c:]
