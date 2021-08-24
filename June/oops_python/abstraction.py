class Student:
    clg_name = 'SIET'
    clg_fee = 85000
    hostel_fee = 75000
    def __init__(self,roll_no,dept):
        self.roll_no = roll_no
        self.dept = dept

    def calculate_fees(self):
        pass

    def student_details(self):
        pass

class Hosteler(Student):

    def __init__(self,roll_no,dept,room_no):
        self.room_no = room_no
        Student.__init__(self,roll_no,dept)
    """python does not have interface for that we must implement all the abstract method of the base class"""
    """I we didn't implement any one of the abstract methods from the base class then the sub class also be considered as abstract class"""
    def calculate_fees(self):
        return (self.clg_fee + self.hostel_fee)

    def student_details(self):
        print("College Name: " + self.clg_name)
        print("roll_no: " + str(self.roll_no))
        print("dept: " + str(self.dept))
        print("Hostel Room No : " + str(self.room_no))

s1 = Hosteler('18cse30','CSE',112)
s1.student_details()
print(s1.calculate_fees())
print(type(s1))