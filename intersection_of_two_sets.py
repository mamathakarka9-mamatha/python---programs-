#finding intersection of two sets s1 and s2
s1 = set(input("Enter your set s1 elements:").split())#creating s1 from user input
s2 = set(input("Enter your set s2 elements:").split())#creating s2 from user input
result = s1.intersection(s2)#intersection of two sets s1 and s2
print("The set s1:", s1)#displaying the sets s1 and s2
print("The set s2:", s2)#displaying the sets s1 and s2 
print("The sets s1 and s2 after intersection:", result)#displaying this message after the intersection of two sets s1 and s2