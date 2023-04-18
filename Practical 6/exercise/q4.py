# program to get the smallest number from a list.
l1=[1,2,3,7,9,8,6,4,5]
i=0
j=1
print("list is",l1)
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]>l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print("The smallest number in the list is:",l1[-1])