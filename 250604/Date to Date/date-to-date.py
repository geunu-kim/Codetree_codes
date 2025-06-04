m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tot_1 = 0 ; m, d = 1, 1 ; j = 1

while True :
    if m == m1 and d == d1 :
        break
    d += 1
    tot_1 += 1
    if d == months[j] :
        m += 1
        d = 1
        j += 1
        tot_1 += 1

tot_2 = 0 ; m, d = 1, 1 ; j = 1

while True :
    if m == m2 and d == d2 :
        break
    d += 1
    tot_2 += 1
    if d == months[j] :
        m += 1
        d = 1
        j += 1
        tot_2 += 1

print(tot_2 - tot_1 + 1)