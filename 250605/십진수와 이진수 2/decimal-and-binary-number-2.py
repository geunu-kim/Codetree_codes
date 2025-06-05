N = input() ; num = 0

# Please write your code here.
for i in range (len(N)) :
    num = num * 2 + int(N[i])

num *= 17

arr = []

while True :
    if num < 2 :
        arr.append(num)
        break
    
    arr.append(num % 2)
    num //= 2

for elem in arr [::-1] :
    print(elem, end="")