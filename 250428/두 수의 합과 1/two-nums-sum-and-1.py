a , b = input().split()

a = int(a)
b = int(b)

c = a + b
cnt = 0

c = str(c)

for i in range (len(c)) :
    if c[i] == "1" :
        cnt += 1

print(cnt)