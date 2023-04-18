set1 = {0,1,2,3,4,5}
set2 = {5,6,7,8,9,0}
set3=set1.intersection(set2)
print("Intersection of set1 and set2:",set3)
set3=set1.union(set2)
print("union of set1 and set2:",set3)
set3=set1.difference(set2)
print("difference of set1 and set2:",set3)
set3=set1.symmetric_difference(set2)
print("symmetric_difference of set1 and set2:",set3)
set1.clear()
print("difference of set1 and set2:",set1)