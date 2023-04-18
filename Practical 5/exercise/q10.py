a = input("enter the number:")
res = str(a) == str(a)[::-1]
if str(res)==1:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")
