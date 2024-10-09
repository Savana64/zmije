class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._grades=[]

    def print_age(self):
        print(self._age)

    def add_grade(self,_grade):
        self._grades.append(_grade)

    def grade_avg(self):
        return sum(self._grades)/ len(self._grades)
   

student = Student("Petr",10)

print(student._name)
student.age = 20
print(student._age)
student.add_grade(12)
print (student._grades)
