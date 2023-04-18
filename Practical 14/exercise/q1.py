class class1:
 def printv1(self, number,word):
     print(number,"and",word)
class class2(class1):
 def printv1(self,word,number):
     print(number,"and",word)
obj=class2()
obj.printv1("Abhishek",49)
obj.printv1(49,"Sinha")
