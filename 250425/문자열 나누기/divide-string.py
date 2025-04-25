n = int(input())
a = list(map(int, input().split()))

c = ''.join(str(elem) for elem in a)

q = len(c)
p = 0
while True :
    print(c[p:p+5:])
    p += 5
    if (p+5) > q :
        print(c[p::])
        break