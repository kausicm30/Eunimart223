class Student:
    clg_name = "SIET"
    def __init__(self, roll_no):
        self.roll_no = roll_no
    def display_details(self):
        print("Student Roll no : " + str(self.roll_no))

#object
s1 = Student(30)
s1.display_details()

#without create a object
print(Student.clg_name)