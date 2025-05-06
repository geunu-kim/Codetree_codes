a, b = map(int, input().split())

# Please write your code here.

def prime(n) :
    for i in range (2,n) :
        if n % i == 0 :
            return False
        else :
            continue
    sum_of_digits = sum(int(digit) for digit in str(n))
    if sum_of_digits % 2 == 0 :
        return True


cnt = 0

for j in range (a,b+1) :
    if prime(j) :
        cnt += 1
    else :
        continue

print(cnt)

