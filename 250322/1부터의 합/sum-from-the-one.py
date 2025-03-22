N = int(input())
prod = 0

for _ in range (1, 101) :
    prod += _
    if prod >= N :
        print(_)
        break