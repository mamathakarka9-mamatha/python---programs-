#checking whether a given number is even number or odd number
n = int(input("Enter your number: "))#using type casting converting string into integer
base = int(input("Enter your base number: "))#using type casting converting string into integer
power= int(input("Enter your power number: "))
result = base**power
print("result:", result)
if result%2==0:
    print("result is an even number")
elif result%2!=0:
    print("result is an odd number")
print("n:", n)
if n%2==0:
    print("n is an even numbers")
elif n%2!=0:
    print("n is an odd numbers")