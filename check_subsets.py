#checking whether two sets s1 and s2 are subset or not
s1 = set(input("Enter your set1 elements:").split())#creating set s1 from user input
s2 = set(input("Enter your set2 elements:").split())#creating set s2 from user input
print("The set s1:", s1)#displaying set s1
print("The set s2:", s2)#displaying set s2
result1 = s1.issubset(s2)#checking whether set s1 is subset of s2 or not
print("The s1 subset of s2:", result1)#displaying result
result2 = s2.issubset(s1)#checking whether set s2 is subset of s1 or not
print("The s2 subset of s1:", result2)#displaying result
