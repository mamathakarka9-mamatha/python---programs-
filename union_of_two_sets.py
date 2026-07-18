#finding union of two sets s1 and s2 
s1 = set(input("enter your set1 elements: ").split())#creating set s1 from user input
s2 = set(input("enter your set2 elements: ").split())#creating set s2 from user input
result = s1.union(s2)#union of sets s1 and s2
print("The set s1:", s1)#displaying set s1
print("The set s2:", s2)#displaying set s2 
print("The union of sets s1 and s2: ", result)#displaying this message after union of two sets s1 and s2   