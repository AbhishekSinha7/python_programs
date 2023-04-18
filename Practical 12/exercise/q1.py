#Roll no:49 Name:Abhishek Sinha
#Write a Python program to create a user defined module that will ask your college name and will display the name of the college.

'''module1.py:
def PrintCollegeName(n):
    print("The college name is:",n)'''

import module1
Name=input("enter the name of your college:")
module1.PrintCollegeName(Name)

'''
Output:
enter the name of your college:RSM POLYTECHNIC
The college name is: RSM POLYTECHNIC
'''