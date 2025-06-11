n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)
# Please write your code here.
offset = 1000
num_1 , num_2 = 0 , 0
arr = [0] * 2001

for i in range (n) :
    if dir[i] == "L" :
        num_2 = num_1 - x[i]
        if num_1 > num_2 :
            for j in range (num_2 , num_1) :
                arr[j + offset] += 1
            num_1 , num_2 = num_2 , num_1
        else :
            for j in range (num_1 , num_2) :
                arr[j + offset] += 1
            num_1 , num_2 = num_2 , num_1
    elif dir[i] == "R" :
        num_2 = num_1 + x[i]
        if num_1 > num_2 :
            for j in range (num_2 , num_1) :
                arr[j + offset] += 1
            num_1 , num_2 = num_2 , num_1
        else :
            for j in range (num_1 , num_2) :
                arr[j + offset] += 1
            num_1 , num_2 = num_2 , num_1

cnt = 0

for elem in arr :
    if elem >= 2 :
        cnt += 1
print(cnt)