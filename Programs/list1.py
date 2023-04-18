a=[]#empty list
print(a)
a=[1,2,3,4,6]#list with elements
print(a)
a=list([])#defining empty list using list function
print(a)
a=list([1,2,3,5,6])#defining list with elements with list function
print(a)

#acess 1st element 
print(a[0])
#acess last element
print(a[-1])


#built in functions
print(len(a))
print(max(a))
print(min(a))
tuple1=(1,2,3,4)
tuple2=list(tuple1)
print(tuple2)


#methods used in only list class
a=[1,2,3,4,5]
print(a)
#add single element
a.append(6)
print(a)
#add multiple elements
a.extend([7,8])
print(a)
#add any single element anywhere 
a.insert(1, 8)
print(a)
#check the element count in list
print(a.count(6))
#get the elemnt at provided index
print(a.index(5))
#remove elements using index
a.pop(1)
#remove elements using element value
a.remove(5)
#remove element using del keyword
del a[2]
print(a)
#sort the list
a.sort()
print(a)
#reverse a list
a.reverse()
print(a)
#delete list
del a
