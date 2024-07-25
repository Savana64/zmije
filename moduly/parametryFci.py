x = 4 #příkaz
print()#příkaz
if True:
    pas 
while False:
    pass
# sekvence příkazů

def foo(): #fce pro opakování) foo = ukázka
    x = 5
    print("Ajoj",x)

foo() # a provede mi to kolikrát ji zavolám
foo() # atd
# parametry
def foo(pozdraf):  # teď mám parametr (pozdraf)
    x = 5
    print(pozdraf, x)

foo ("Ahoj") # teď ti napíše Ahoj 5 
foo("Nazdar") # napíše Nazdar, chápeš
# fce něco vrací nebo  něco mění
def count_seconds(hours: int, minutes: int, seconds: int) -> int:
    return 3600  *  hours + 60 * minutes + seconds
    # tady už nic nezrobí bo má nad tímhle return
total_seconds = count_seconds(1,11,4) # total_seconds = 4264

# oop
students =[]

def  add_student( students, new_student_name, new_students_grades):
    student_dic = {
        "name": new_student_name # atd

    }
# nebo si zrobím klas
    
class Student:
    ""
    #třída co ví o studentech všechno"""

    def __init__(self, name) -> None: # tu nima parametr grades bo je nejdřív pro všewchny stejný, default
        self.name = name
        self.grades= []  

    def add_grade(self, new_grade: int) -> None:
        self.grades.append(new_grade)

pepa = Student("Pepa")
pepa.add_grade(1) # pepa dostal jedničku

class Foo:
    def __init__(self, name,  l):
        self.name = name
        self.grades = []
        l.append(self)
        
    

