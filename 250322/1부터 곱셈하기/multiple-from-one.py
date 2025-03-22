N = int(input())
prod = 1

for _ in range (1, 11) :
    prod *= _
    if prod >= N :
        print(_)
        break

