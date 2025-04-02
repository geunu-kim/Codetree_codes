N = int(input())
cnt_1 = 1 ; cnt_2 = 0 ; arr = []

while True :
    arr.append(N * cnt_1)
    cnt_1 += 1
    if arr[-1] % 5 == 0 :
        cnt_2 += 1
        if cnt_2 == 2 :
            break

for elem in arr :
    print(elem, end=" ")
    
