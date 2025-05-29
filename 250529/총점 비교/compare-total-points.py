n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range (n) :
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Student :
    def __init__ (self,a,b,c,d) :
        self.name = a
        self.s1 = b
        self.s2 = c
        self.s3 = d

Students = [
    Student(name[i],score1[i],score2[i],score3[i]) for i in range (n)
]

Students.sort(key = lambda x : x.s1 + x.s2 + x.s3)

for Student in Students :
    print(Student.name, Student.s1, Student.s2, Student.s3)
