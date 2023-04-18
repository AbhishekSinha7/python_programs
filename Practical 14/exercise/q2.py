class Square:
    def _init_(self):
        pass 
      
    def Area1(self,side=None):
        if (side!=None):
            area=side*side
            print("Area of Square:",area)
    
    def Area1(self,length=None,breadth=None):
        if (length!=None and breadth!=None):  
            area=length*breadth
            print("Area of Rectangle:",area)

s1=Square()
s1.Area1(5)
s1.Area1(6,3)