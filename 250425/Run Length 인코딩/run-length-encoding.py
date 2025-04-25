A = input()

# Please write your code here.
B = [] ; cnt = 1

for i in range (len(A)) :
    if i < (len(A) - 1) :
        if A[i] == A[i+1] :
            cnt += 1
            continue
    if i < (len(A) - 1) :
        if A[i] != A[i+1] :
            B.append(A[i])
            B.append(cnt)
            cnt = 1
    if i == (len(A) - 1) :
        B.append(A[i])
        B.append(cnt)

result = ''.join(str(num) for num in B)
print(len(result))
print(result)

