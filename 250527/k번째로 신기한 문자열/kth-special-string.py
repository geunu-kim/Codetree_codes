n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
sorted_str = sorted(str)
str2 = []

for elem in sorted_str :
    if t in elem :
        str2.append(elem)

for elem in str2 :
    if elem[:len(t):] == t :
        continue
    else :
        str2.remove(elem)

sorted_str2 = sorted(str2)

print(sorted_str2[k-1])