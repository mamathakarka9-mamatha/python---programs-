# Create and display a copy of set s1 s times
s1 = set(input("Enter your set s1 elements: ").split())#creating set s1 from user input
s = int(input("Enter how many times you need to copy: "))#enter how many times you need to copy original set s1
if s == 0:#checking if s is equal to zero
    print("The set after copying set s1: ", s1)#displaying the set s1 
elif s < 0:#checking if s is less than zero
   print("s should not be negative")#display this message if s is less than zero 
else:
 for i in range(s):#looping the s1 until the conition is true
    s2 = s1.copy()#copying the set elements 
    print("The set after copying set s1: ", s2)#displaying the set s2 after copying set s1 