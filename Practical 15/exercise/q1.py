class Employee:
    name=""
    department=""
    salary=""
    
    def getdata(self):
        name=input("enter your name:")
        department=input("enter your department:")
        salary=input("enter your salary:")

    def putdata(self):
        print("name:",self.name)
        print("department:",self.department)
        print("salary:",self.salary)

obj=Employee()
obj.getdata()
obj.putdata()
