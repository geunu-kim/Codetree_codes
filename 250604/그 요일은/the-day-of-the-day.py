m1, d1, m2, d2 = map(int, input().split())
A = input() ; tot = 0 ; tot_1 , tot_2 = 0 , 0

# Please write your code here.
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]
B = day.index(A)

for i in range (m1) :
    tot_1 += months[i]
tot_1 += d1

for i in range (m2) :
    tot_2 += months[i]
tot_2 += d2

for i in range(tot_2 - tot_1 + 1):  # 시작일 포함
    if i % 7 == B:
        tot += 1

print(tot)
