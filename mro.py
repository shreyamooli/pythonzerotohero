#method resolution order uses c3 linearization algo
#goes from left to right

class father():
    def drive(self):
        print("father drives")

class mother():
    def drive(self):
        print("mother drives")

class child(mother,father): #mro goes from left to right
    def drive(self):
        print("child drives") #method overriding - run time polymorphism
        super().drive() #super follows mro

o1=child()
o1.drive()
