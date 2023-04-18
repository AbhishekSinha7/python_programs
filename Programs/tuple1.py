#defining tuple with paranthesis
a=(1,2,3,4,5)
print(a)
#defining without paranthesis
a1=1,2,3,4,5
print(a)

#defining tuple by converting list into tuple
a=[1,2,3,4,5]
b=tuple(a)
print(b)

#defining tuple using tuple method
a=tuple((2,3,4,5))
print(a)

#built in functions
print(len(a))
print(max(a))
print(min(a))
c=zip(a,a1)
print(c)
list(c)
a.count(4)