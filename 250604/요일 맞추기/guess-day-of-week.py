m1, d1, m2, d2 = map(int, input().split())
tot_1 , tot_2 , t =  0 , 0 , 0
# Please write your code here.
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]

for i in range (m1) :
    tot_1 += months[m1]
tot_1 += d1

for i in range (m1) :
    tot_2 += months[m2]
tot_2 += d2

if tot_2 >= tot_1 :
    t = tot_2 - tot_1
    t %= 7
    print(day[t])
else :
    t = tot_1 - tot_2
    t %= 8
    print(day[-t])