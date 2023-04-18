def check(s):
    d={"uppercase":0, "lowercase":0}
    for c in s:
        if c.isupper():
           d["uppercase"]+=1
        elif c.islower():
           d["lowercase"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No of Upper case characters: ", d["uppercase"])
    print ("No of Lower case Characters: ", d["lowercase"])
str1=input("Enter the string:")
check(str1)
