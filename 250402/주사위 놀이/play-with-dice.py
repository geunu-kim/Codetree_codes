new_arr = [0] * 7

arr = list(map(int, input().split()))

for elem in arr :
    new_arr[elem] += 1

for i in range (6) :
    print(f"{i+1} - {new_arr[i+1]}")

