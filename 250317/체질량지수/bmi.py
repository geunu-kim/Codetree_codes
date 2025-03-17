A = input().split()

h = int(A[0])
w = int(A[1])

b = (10000 * w) / (h * h)

print(int(b))
if b >= 25 :
    print("Obesity")

