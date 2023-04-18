#Roll no:49 Name:Abhishek Sinha
# Write a program to calculate surface volume and area of a cylinder.

pi=3.141592653589793238
radius=input("enter the radius:") 
height=input("enter the height:") 
radius=int(radius)
height=int(height)
volume=pi*radius*radius*height
Area=(2*pi*radius*height)+(2*pi*radius*radius)
print("The Volume of cylinder is:",volume)
print("The Area of cylinder is:",Area)

'''Output:
enter the radius:7
enter the height:5
The Volume of cylinder is: 769.6902001294993
The Area of cylinder is: 527.7875658030853
'''