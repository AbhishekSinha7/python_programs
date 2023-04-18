#Roll no:49 Name:Abhishek Sinha
# Write a program to convert bits to Megabytes, Gigabytes and Terabytes

Bits=input("enter value in bits:")
Bits=int(Bits)
Megabytes=Bits/8388608
Gigabytes=Bits/8589934592
Terabytes=Bits/8796093022208

print("Megabytes:",Megabytes)
print("Gigabytes:",Gigabytes)
print("Terabytes:",Terabytes)

'''
Output:
enter value in bits:10324803
Megabytes: 1.230812430381775     
Gigabytes: 0.001201965264044702  
Terabytes: 1.1737942031686543e-06
'''