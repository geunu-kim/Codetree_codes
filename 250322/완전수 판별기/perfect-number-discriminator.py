N = int(input())
cnt = 0

for _ in range (1,N) :
    if N % _ == 0 :
        cnt += _ 

if cnt == N :
    print("P")
else :
    print("N")