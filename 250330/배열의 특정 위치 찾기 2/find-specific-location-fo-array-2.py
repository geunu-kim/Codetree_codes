arr = list(map(int, input().split())) ; sum_even = 0 ; sum_odd = 0

for elem in arr[1::2] :
    sum_even += elem

for elem in arr[0::2] :
    sum_odd += elem

if sum_even > sum_odd :
    print(sum_even - sum_odd)
else :
    print(sum_odd - sum_even)


