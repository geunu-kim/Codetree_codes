N = int(input())
arr = list(map(int,input().split()))
new_arr = [0] * 10

for elem in arr :
    new_arr[elem] += 1

del new_arr[0]

for elem in new_arr :
    print(elem)


