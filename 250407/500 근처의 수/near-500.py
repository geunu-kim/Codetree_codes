arr = list(map(int, input().split()))
a = 0 ; b = 1000

for elem in arr :
    if elem < 500 :
        if elem > a :
            a = elem
    else :
        if elem < b :
            b = elem
            

print(a,b)