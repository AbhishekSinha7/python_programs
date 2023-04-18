#Roll no:49 Name:Abhishek Sinha
#Dictionary operations
#Creating dictionary
Abhishek =	{
  "Age": "18",
  "Grade": "A",
  "hobby": "watching Animation"
}
#print dictionary items
print("dictionary items:",Abhishek)
#print specific dictionary keys and their values
print("Displaying key - Age:")
print(Abhishek["Age"])
#print dictionary keys
print("Displaying all dictionary keys:")
print(Abhishek.keys())
#print dictionary Values
print("Displaying all dictionary Values:")
print(Abhishek.values())
#UPdating dictionary Values
Abhishek.update({"hobby": "Coding"})
print(Abhishek)
#Looping through dictionary
for x, y in Abhishek.items():
  print(x, y)
#deleting dictionary
del Abhishek
print("After deleting dictionary")
print(Abhishek)
'''
Output:dictionary items: {'Age': '18', 'Grade': 'A', 'hobby': 'watching Animation'}
Displaying key - Age:
18
Displaying all dictionary keys:
dict_keys(['Age', 'Grade', 'hobby'])
Displaying all dictionary Values:
dict_values(['18', 'A', 'watching Animation'])
{'Age': '18', 'Grade': 'A', 'hobby': 'Coding'}
Age 18
Grade A
hobby Coding
After deleting dictionary
Traceback (most recent call last):
  File "e:\python\Practical 9\dict_operations.py", line 27, in <module>
    print(Abhishek)
NameError: name 'Abhishek' is not defined'''