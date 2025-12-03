class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"His / Her name is {self.name} and is {self.age} years old"
    
    
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        print(f"The students name is {self.name}, {self.age} years old with a student id of {self.student_id} taking {self.course}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        print(f"The teachers name is {self.name} taking {self.subject} with a salary of Ksh. {self.salary}")

    
student1 = Student("Sophie", 18, 234, "Business Administration")
student1.display_info()
teacher1 = Teacher("Morgan", 28, "Biology", 45000)
teacher1.display_info()



        
        