#finding the difference between the two sets
s1 = set(input("Enter your set s1 elements: ").split())#creating a set s1 from user input
s2 = set(input("Enter your set s2 elements: ").split())#creating a set s2 from user input
print("The set s1:", s1)#displaying the set s1
print("The set s2:", s2)#displaying the set s2
result1 = s1.difference(s2)#finding the difference of set s1 from s2
print("The difference of set s1 from s2: ", result1)#displaying the result
result2 = s2.difference(s1)#finding the difference of set s2 from s1
print("The difference of set s2 from s1: ", result2)#displaying the result