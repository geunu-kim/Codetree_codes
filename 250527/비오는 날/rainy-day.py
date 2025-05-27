n = int(input())
date = []
day = []
weather = []
cnt = [] ; cnt_2 = []

for _ in range(n) :
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Future :
    def __init__ (self,a,b,c) :
        self.d = a
        self.dy = b
        self.w = c

for i in range (len(weather)) :
    if weather[i] == "Rain" :
        cnt.append(i)
    else :
        continue

for elem in cnt :
    cnt_2.append(date[elem])

sorted_cnt_2 = sorted(cnt_2) ; really = cnt_2.index(sorted_cnt_2[0])
really_2 =  date.index(cnt_2[really])

Future_2 = Future(date[really_2],day[really_2],weather[really_2])

print(Future_2.d,Future_2.dy,Future_2.w)