class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi my name is {self.name} , I am {self.age} old.")

class Student:
    def __init__(self,school,grade):
        self.school = school
        self.grade = grade
class Doctor:
    def __init__(self,hname,spec):
        self.hname = hname
        self.spec = spec

my_person = Person("Bagdat",18)
my_student = Student("145",5)
my_doctor = Doctor("Maksutov", "surgeon")
print(my_person.name)
print(my_student.grade)
print(my_doctor.spec)
print(my_person.introduce())