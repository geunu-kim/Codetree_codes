n = int(input()) ; cnt = 0 ; sum_val = 0

for i in range (n) :
    arr = list(map(int, input().split()))
    for elem in arr :
        sum_val += elem
    if sum_val / len(arr) >= 60 :
        print("pass")
        cnt += 1
        sum_val = 0
    else :
        print("fail")
        sum_val = 0

print(cnt)
    