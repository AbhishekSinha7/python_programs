x=10
while x>5:
 print x,
 x-=1

 '''
 Output:  print x,
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, end=" ")?'''