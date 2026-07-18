#check whether given two sets are disjoint or not 
s1 = set(input("Enter your set s1 elements: ").split())#creating set s1 from user input
s2 = set(input("Enter your set s2 elements: ").split())#creating set s2 from user input
print("The set s1:", s1)#displaying set s1
print("The set s2:", s2)#displaying set s2
result1 = s1.isdisjoint(s2)#checking if sets are disjoint
print("The two sets after the disjoint of s1 and s2:", result1)#displaying result