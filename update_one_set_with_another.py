#update one set with another set
s1 = set(input("Enter your set1 elements:").split())#creating set s1 from user input
s2 = set(input("Enter your set2 elements:").split())#creating set s2 from user input
print("The set s1:", s1)#displaying set s1
print("The set s2:", s2)#displaying set s2
s1.update(s2)#updating set s1 with elements of set s2
print("The updated set s1:", s1)#displaying updated set s1
s2.update(s1)#updating set s2 with elements of set s1
print("The updated set s2:", s2)#displaying updated set s2 