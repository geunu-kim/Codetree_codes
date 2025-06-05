n = int(input())
# Please write your code here.
array = []

while True :
    if n < 2 :
        array.append(n)
        break
    
    array.append(n % 2)
    n //= 2

for elem in array [::-1] :
    print(elem, end="")