A = input()
B = input()
cnt = 0

for i in range (len(A)) :
    A = A[-1] + A[:-1]
    if A == B :
        cnt += 1
        break
    else :
        cnt += 1

if cnt == len(A) :
    print(-1)
else :
    print(cnt)


