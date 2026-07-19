#creating set from user input and converting set into list and tuple
elements = input("Enter your set elements: ").split()#taking input from user and splitting it into list
s = set(elements)
print("The set:", s)
lst = list(s)#converting set s into list
#converting set into list
print("The set after converting into list:", lst)#printing list
#converting set s into tuple
name = tuple(s)#converting set into tuple
print("The set after converting into tuple:", name)#printing tuple 