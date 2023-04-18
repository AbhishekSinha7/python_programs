#program to select the even items of a list.
l1=[1,2,3,4,5]
l2=[]
for i in range(len(l1)):
    if l1[i]%2==0:
        l2.append(l1[i])
print(l2)