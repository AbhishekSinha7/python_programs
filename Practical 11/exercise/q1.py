def prime(num):
    if num>1:
        s=int(num/2)
        for i in range(2,s+1):
            if num%i==0:
                return("The number is not prime")
                break
        return("The number is prime")
num=int(input("enter the number:"))
print(prime(num)) 
