#factorial of a number
n = int(input("enter your number: ")) #by using type casting converting input string into integer
factorial = 1
if n<0:
    print("factorial doesnot exist")
elif n==0:
    print("factorial is 1")
elif n>0:
 for i in range(1, n+1):
    factorial = factorial*i
    print(factorial)