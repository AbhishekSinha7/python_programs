class Degree:
    def getDegree(self):
        print("I got a degree...")
class Undergraduate(Degree):
    def graduate(self):
        print("I am an Undergraduate...")
class Postgraduate(Degree):
    def graduate(self):
        print("I am Postgraduate...")

obj1=Undergraduate()
obj1.getDegree()
obj1.graduate()

obj2=Postgraduate()
obj2.graduate()