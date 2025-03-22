b = "1"
for _ in range (5) :
    a = int(input())
    if a % 3 != 0 :
        b = "0"
        break
    else :
        continue
print(b)