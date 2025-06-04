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

t = tot_2 - tot_1

for i in range(1, t + 1):  # 시작일부터 끝일까지 포함
    if (B + i) % 7 == 0:
        tot += 1

print(tot)