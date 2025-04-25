a = input()
cnt_1 , cnt_2 = 0 , 0

for i in range (len(a) - 1) :
    if a[i] == "e" and a[i+1] == "e" :
        cnt_1 += 1
    if a[i] == "e" and a[i+1] == "b" :
        cnt_2 += 1

print(cnt_1,cnt_2)