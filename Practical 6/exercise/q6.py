# program to find common items from two lists
l1=[1,2,4,5]
l2=[3,5,6,7]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            temp=l1[i]
print(temp)