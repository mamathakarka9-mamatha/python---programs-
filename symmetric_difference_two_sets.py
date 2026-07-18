#finding the symmetric difference between two sets 
s1 = set(input("Enter your set s1 elements: ").split())#creating set s1 from user input
s2 = set(input("Enter your set s2 elements: ").split())#creating set s2 from user input
print("The set s1: ", s1)#displaying set s1
print("The set s2: ", s2)#displaying set s2
result1 = s1.symmetric_difference(s2)#finding the symmetric difference between two sets s1 and s2
print("The symmetric difference between two sets s1 and s2: ", result1)#displaying the result