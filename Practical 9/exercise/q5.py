dict ={"V":"S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}
list =[] 
for val in dict.values(): 
  if val in list: 
    continue 
  else:
    list.append(val)
print(list)