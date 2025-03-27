arr_list = list(map(int,input().split())) ; total = 0 ; cnt = 0

for elem in arr_list :
    if elem < 250 :
        total += elem
        cnt += 1
    else :
        average = total / cnt
        print(f"{total} {average:.1f}")
        exit()

print(f"{total} {average:.1f}")


