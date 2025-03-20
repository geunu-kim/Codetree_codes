N = int(input())
cnt = 0

for _ in range (1,N+1) :
    if _ % 100 == 0 and _ % 400 != 0 :
        None
    elif _ % 4 == 0 :
        cnt += 1

print(cnt)
    