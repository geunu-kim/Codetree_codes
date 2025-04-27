A = input()
B = input()

# Please write your code here.
while B in A :
    C = A.find(B)
    a = list(A)
    b = list(B)
    del a[C:C+len(b):]
    A = ''.join(a)

print(A)