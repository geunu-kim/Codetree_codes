N = int(input())
sum_val = 0

for _ in range (N) :
    a = int(input())
    if a % 2 == 1 and a % 3 == 0 :
        sum_val += a

print(sum_val)

