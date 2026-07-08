#simple calculator
a = float(input("enter your first number: ")) #by using type casting converting input string into float
b = float(input("enter your second number: ")) #by using type casting converting input string into float
print("addition:", a+b)
print("substraction:", a-b)
print("multiplication:", a*b)
print("power:", a**b)
if b!=0:
 print("division:", a/b)
 print("floor division:", a//b)
else:
 print("cannot divided by zero")