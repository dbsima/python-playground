class Parent():
    def __init__(self, last_name, eye_color):
        print 'Parent constructor called'
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print "Last name - "+self.last_name
        print "Eye color - "+self.eye_color

# Class Child inherites Parent
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print 'Child constructor called'
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    
    # override method
    def show_info(self):
        print "Last name - "+self.last_name
        print "Eye color - "+self.eye_color
        print "No of toys - "+str(self.number_of_toys)

dragos_sima = Parent("Sima", "green")
dragos_sima.show_info()

chitac_sima = Child("Sima", "blue", 4)
chitac_sima.show_info()