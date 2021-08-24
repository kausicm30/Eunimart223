class Owner:
    def __init__(self,owner_name):
        self.owner_name = owner_name

class Theatre(Owner):
    def __init__(self,theatre_name,owner_name):
        self.theatre_name = theatre_name
        Owner.__init__(self,owner_name)

class Movie(Theatre):
    def __init__(self,movie_name,theatre_name,owner_name):
        self.movie_name = movie_name
        Theatre.__init__(self,theatre_name,owner_name)
    def diplay_details(self):
        print("Owner Name : " + str(self.owner_name))
        print("Theatre Name : " + str(self.theatre_name))
        print("Movie Name : " + str(self.movie_name))

m1 = Movie('Master', 'Pheonix Theatre','Kausic')
m1.diplay_details()