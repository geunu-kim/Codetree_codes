n = 5
n = int(n)
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class student :
    def __init__ (self, name, height, weight) :
        self.n = name
        self.h = height
        self.w = weight

students = [
    student(name[i], height[i], weight[i]) for i in range (5)
]

students.sort(key = lambda x : x.n)

print("name")
for student in students :
    print(student.n , student.h , student.w)
print()

students.sort(key = lambda x : -x.h)

print("height")
for student in students :
    print(student.n , student.h , student.w)