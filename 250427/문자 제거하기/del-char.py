a = input()
b = list(a)

for i in range (len(b) - 1) :
    c = int(input())
    if c < len(b) :
        b.pop(c)
        d = ''.join(b)
        print(d)
    else :
        b.pop(-1)
        d = ''.join(b)
        print(d)

  