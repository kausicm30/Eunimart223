class Student:
    #protected
    _name = None
    _roll_no = None
    def __init__(self, name, roll_no):
        self._name = name
        self._roll_no = roll_no

    #private method
    def __details(self):
        print("Name: ", self._name)
        print("Roll: ", self._roll_no)

    def displaydetails(self):
        self.__details()

class Hosteller(Student):
    def __init__(self, name, roll_no):
        Student.__init__(self, name, roll_no)

s1 = Hosteller('Kausic', '!8cse30')
print(s1._roll_no)

s1.displaydetails()

#private method cannot be accessed by subclass
s1.__details()