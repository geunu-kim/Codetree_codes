binary = input() ; num = 0

# Please write your code here.
for i in range (len(binary)) :
    num = num * 2 + int(binary[i])

print(num)