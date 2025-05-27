n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
sorted_str = sorted(str)
str2 = []

for elem in str :
    if t in elem :
        str2.append(elem)

sorted_str2 = sorted(str2)

print(sorted_str2[k-1])