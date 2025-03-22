A = int(input())

for _ in range (1,A+1) :
    if (_ % 2 == 0 and _ % 4 != 0) or ((_ // 8) % 2 == 0) or ((_ % 7) < 4) :
        continue
    print(_, end=" ")

