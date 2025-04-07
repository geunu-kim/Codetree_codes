n = int(input())
a = list(map(int, input().split()))
cnt = 1000000000

for i in range (n) :
    for j in range (n) :
        if a[i] > a[j] :
            if a[i] - a[j] <= cnt :
                cnt = a[i] - a[j]
            else :
                pass
        elif a[i] < a[j] :
            if a[j] - a[i] <= cnt :
                cnt = a[j] - a[i]
            else :
                pass
        else :
            pass

print(cnt)


