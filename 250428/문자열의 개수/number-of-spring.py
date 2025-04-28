b = []
cnt = 0

while True :
    a = input()
    if a == "0" :
        break
    else :
        b.append(a)
        cnt += 1

print(cnt)
for i in range (len(b)) :
    if i % 2 == 0 :
        print(b[i])
    else :
        continue

