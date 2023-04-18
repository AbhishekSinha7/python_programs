#Roll no:49 Name:Abhishek Sinha
# Tuple operations
tuple1 = ("java", "python", "javascript", "php")
#print tuple items
print("tuple items:",tuple1)
#print tuple items from index 1 to 2
print("items from index 1 to 2:",tuple1[1:3])
#print tuple item on index 3
print("item on index 3:",tuple1[3])
#removing elements from tuple
print("removing php from tuple:")
y = list(tuple1)
y.remove("php")
tuple1 = tuple(y)
print(tuple1)
#deleting list
del tuple1
print("After deleting tuple")
print(tuple1)#trying to acess after deleting

'''
Output:
tuple items: ('java', 'python', 'javascript', 'php')
items from index 1 to 2: ('python', 'javascript')
item on index 3: php
removing php from tuple:
('java', 'python', 'javascript')
After deleting tuple
Traceback (most recent call last):
  File "e:\python\Practical 7\tuple_operations.py", line 22, in <module>
    print(tuple1)#trying to acess after deleting
NameError: name 'tuple1' is not defined'''