arr = ["apple","banana","grape","blueberry","orange"]
a = len(arr)

b = input()
cnt = 0

for i in range (a) :
    if arr[i][2] == b or arr[i][3] == b  :
        cnt += 1
        print(arr[i])

if cnt == 0 :
    print(0)
else :
    print(cnt)

