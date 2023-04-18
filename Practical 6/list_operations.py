#Roll no:49 Name:Abhishek Sinha
# List operations
list1 = ["java", "python", "javascript", "php"]
#print list items
print("list items:",list1)
#print list items from index 1 to 2
print("items from index 1 to 2:",list1[1:3])
#print list item onc index 3
print("item on index 3:",list1[3])
#adding elemet in the list
print("adding element in the list")
list1.append("angular")
print(list1)
#adding element at index 2
print("adding element at index 2:")
list1.insert(2, "nodejs")
print(list1)
#removing nodejs from list
print("removing nodejs from list:")
list1.remove("nodejs")
print(list1)
#removing element at index 4
print("removing element at index 4:")
list1.pop(4)
print(list1)
#deleting list
del list1
print("After deleting list")
print(list1)#trying to acess after deleting
'''
Output:
list items: ['java', 'python', 'javascript', 'php']
items from index 1 to 2: ['python', 'javascript'] 
item on index 3: php
adding element in the list
['java', 'python', 'javascript', 'php', 'angular']
adding element at index 2:
['java', 'python', 'nodejs', 'javascript', 'php', 'angular']
removing nodejs from list:
['java', 'python', 'javascript', 'php', 'angular']
removing element at index 4:
['java', 'python', 'javascript', 'php']
After deleting list
Traceback (most recent call last):
  File "e:\python\Practical 6\list_operations.py", line 34, in <module>
    print(list1)#trying to acess after deleting
NameError: name 'list1' is not defined
'''