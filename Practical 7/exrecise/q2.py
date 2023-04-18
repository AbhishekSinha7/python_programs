#program to find the repeated items of a tuple.
t1=(1,2,4,4,3,5,7)
for i in range(0, len(t1)):    
    for j in range(i+1, len(t1)):    
        if(t1[i] == t1[j]):    
            print(t1[j]); 