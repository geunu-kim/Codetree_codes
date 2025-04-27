a = input()

b = a.find("e")

A = list(a)

A.pop(b)

F = ''.join(A)

print(F)