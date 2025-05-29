n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Student :
    def __init__ (self,a,b,c,d) :
        self.name = a
        self.korean = b
        self.english = c
        self.math = d

Students = [Student(name[i], korean[i], english[i], math[i]) for i in range (n)]

Students.sort(key = lambda x : (-x.korean, -x.english, -x.math))

for Student in Students :
    print(Student.name, Student.korean, Student.english, Student.math)