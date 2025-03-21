arr = input().split()
a = int(arr[0]) ; b = int(arr[1]) ; sum_val = 0


for _ in range (a,b+1) :
    if _ % 2 == 0 :
        sum_val += _ 

print(sum_val)
