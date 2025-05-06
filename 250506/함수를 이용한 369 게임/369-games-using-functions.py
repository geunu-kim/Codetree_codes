a, b = map(int, input().split())

# Please write your code here.
cnt = 0

def condition(n) :
    if (n // 10) == 3 or (n // 10) == 6 or (n // 10) == 9 or (n % 10) == 3 or (n % 10) == 6 or (n % 10) == 9 or ((n // 10) + (n % 10)) % 3 == 0 :
        return True

for i in range (a,b+1,1) :
    if condition(i) == True :
        cnt += 1

print(cnt)
