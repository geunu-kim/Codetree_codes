n = int(input())
price = list(map(int, input().split()))
cnt = 0 ; idx = 0

for i in range (n) :
    for j in range (i+1,n) :
        if price[j] - price[i] <= 0 :
            pass
        else :
            if price[j] - price[i] > idx :
                idx = price[j] - price[i]

print(idx)