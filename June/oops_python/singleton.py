class Admin:
    instance = None
    def __init__(self):
        if Admin.instance is None:
            Admin.instance = self
        else:
            raise Exception("Only once created an object you can go with that instance")

    @staticmethod
    def get_instance():
        if Admin.instance is None:
            Admin.instance = Admin()
        return Admin.instance
a1 = Admin();
print (a1.instance)
#a2 = Admin();
#print (a2)
a2 = Admin.get_instance()
print (a2.instance)