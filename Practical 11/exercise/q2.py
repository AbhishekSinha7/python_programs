def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)
num=abs(int(input("enter the no:")))
a=factorial(num)
print(a)
