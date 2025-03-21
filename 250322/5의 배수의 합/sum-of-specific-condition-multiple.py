arr = input().split()
a = int(arr[0]) ; b = int(arr[1]) ; sum_val = 0

if a > b :
    for _ in range (b,a+1) :
        if _ % 5 == 0 :
            sum_val += _
elif a == b :
    if a % 5 == 0 :
        sum_val += a
else :
    for _ in range (a,b+1) :
        if _ % 5 == 0 :
            sum_val += _

print(sum_val)
