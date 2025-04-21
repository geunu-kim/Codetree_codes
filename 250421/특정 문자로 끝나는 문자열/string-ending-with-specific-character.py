arr = [] ; cnt = 0

for i in range (10) :
    a = input()
    arr.append(a)

b = input()

for elem in arr :
    if elem[-1] == b :
        print(elem)
        cnt += 1

if cnt == 0 :
    print("None")


