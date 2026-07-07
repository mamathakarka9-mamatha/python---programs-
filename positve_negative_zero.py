#checking whether a given number is positive or negative or zero
n = int(input("enter the number: ")) #by using type casting converting string into integer
if n>0:
    print("n is an positive number")
elif n<0:
    print("n is an negative number")
else:
    print("n is zero")