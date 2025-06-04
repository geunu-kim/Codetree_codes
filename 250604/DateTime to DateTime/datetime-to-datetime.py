a, b, c = map(int, input().split())
tot = 0 ; b2, c2 = 0, 0
# Please write your code here.
if a == 11 :
    if a <= 11 and b <= 11 :
        print(-1)
    else :
        b2 = b - 11 ; c2 = c - 11
        tot = (b2 * 60) + c2
        print(tot)
elif a < 11 :
    print(-1)
else :
    a -= 11 ; b2 = b - 11 ; c2 = c - 11
    tot = (b2 * 60) + (a *1440) + c2
    print(tot)