N = int(input())

for _ in range (1, N+1) :
    if _ % 3 == 0 :
        print(0, end=" ")    
    elif _ % 10 == 3 or _ % 10 == 6 or _ % 10 == 9 :
        print(0, end=" ")
    elif _ // 10 == 3 or _ // 10 == 6 or _ // 10 == 9 :
        print(0, end=" ")
    else :
        print(_,end=" ")
