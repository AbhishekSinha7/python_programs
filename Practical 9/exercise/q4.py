# Python program to find the highest 3 values in a dictionary
diction1={"no1":1,"no2":2,"no3":3,"no4":50,"no6":6,"no7":74,"no5":11,"no8":51,"no9":2,"no10":83,"no11":94,"no12":6,"no13":7,"no14":5}
collect=[]
for i in diction1.values():
    collect.append(i)
collect.sort()
print(collect[-3],collect[-2],collect[-1])
    