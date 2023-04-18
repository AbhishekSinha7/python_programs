# program to get the largest number from a list
l1=[1,2,6,7,8,9,3,4,5]
sum=1
i=0
j=1
temp=0
print("List is",l1)
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]<l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print("The greatest number in the list is:",l1[-1])