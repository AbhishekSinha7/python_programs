# program that takes the marks of 5 subjects and displays the grade.
English=int(input("Enter marks:"))
Hindi=int(input("Enter marks:"))
Marathi=int(input("Enter marks:"))
Maths=int(input("Enter marks:"))
Science=int(input("Enter marks:"))
avg=(English+Hindi+Marathi+Maths+Science)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")