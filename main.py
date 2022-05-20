#complex calculator

type=input("Which data type digit do you choose?")

if type =="float":
   x= float(input('Assign a number for x.'))
   y= float(input('Assign a number for y.'))

else :
   x= int (input("Assign a number for x."))
   y= int (input("Assign a number for y."))

operation= input("enter operation")
if operation== 'addition':
   print(x+y)
elif operation=='subtraction':
   print(x-y)
elif operation=='multiplication':
   print(x*y)
elif operation=='division':
   print(x/y)

solution=(x+y) or (x-y) or (x*y) or (x/y)
complex_solution=complex(solution)

print("the solution of this expression in its complex form is",complex_solution)




