a, b = map(int, input().split())

# Please write your code here.

def if_prime(n) :
    for i in range (2, n) :
        if (n % i) == 0 :
            return False
    return True


tot = 0

for j in range (a,b+1) :
    if if_prime(j) :
        tot += j
    else :
        continue

print(tot)
