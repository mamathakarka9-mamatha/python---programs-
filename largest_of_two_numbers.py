#compare two integers and print the largest number
n = int(input("enter your number: "))#by using type casting converting string into integer
i = int(input("enter your number: ")) #by using type casting converting string into integer
if n>i:
    print("largest number:", n)
elif i>n:
    print("largest number:", i)
else:
    print("both n and i are equal")