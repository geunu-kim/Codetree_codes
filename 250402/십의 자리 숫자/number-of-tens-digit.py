arr = list(map(int, input().split()))
new_arr = [0] * 10

for elem in arr :
    if elem == 0 :
        break
    else :
        new_arr[elem // 10] += 1

for i in range (9) :
    print(f"{i+1} - {new_arr[i+1]}")

