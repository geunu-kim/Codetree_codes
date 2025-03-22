N = int(input())

for _ in range (1,N+1) :
    if _ % 2 == 0 or _ % 10 == 5 or (_ % 3 == 0 and _ % 9 != 0) :
        continue
    else :
        print(_, end= " ")