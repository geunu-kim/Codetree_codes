a = input()
b = len(a)
print(a)
for i in range (b) :
    a = a[-1] + a[:-1]
    print(a)

