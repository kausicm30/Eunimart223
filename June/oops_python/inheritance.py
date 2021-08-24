class Student:
    clg_name = 'SIET'
    clg_fee = 85000
    def __init__(self,roll_no,dept):
        self.roll_no = roll_no
        self.dept = dept

    def student_details(self):
        print("College Name: " + self.clg_name)
        print("roll_no: " + str(self.roll_no))
        print("dept: " + str(self.dept))

class Hosteler(Student):
    hstl_fee = 75000
    def __init__(self,roll_no,dept,room_no):
        self.room_no = room_no
        Student.__init__(self,roll_no,dept)

    def student_details(self):
        print("College Name: " + self.clg_name)
        print("roll_no: " + str(self.roll_no))
        print("dept: " + str(self.dept))
        print("Hostel Room No : " + str(self.room_no))

s1 = Hosteler('18cse30','CSE',112)
s1.student_details()