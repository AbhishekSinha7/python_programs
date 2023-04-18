class A():
  def __init__(self, name):
    self.name = name
  
  # This func will define what happens when adding two obects type A
  def __add__(self, b):
    return (str(self.name) + " " + str(b.name))
  
  # This func will define what happens when converting object to str
  def __str__(self):	# Requested with the print() func
    return self.name

Var1 = A('Gabriel')
Var2 = A('Stone')

Var3 = Var1 + Var2

print(Var1)
print(Var2)
print(Var3)