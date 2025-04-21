n = int(input())
arr = [] ; ave = 0 ; cnt = 0

for i in range (n) :
    a = input()
    arr.append(a)

b = input()

for elem in arr :
    if elem[0] == b :
        cnt += 1
        ave += len(elem)

print(f"{cnt} {(ave / cnt):.2f}")


