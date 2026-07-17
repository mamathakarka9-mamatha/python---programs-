#adding one element to the set
s = set(input("enter your set elements: ").split())#taking input from user 
element = input("enter the element to be added: ")#taking input from user for the element to be added
s.add(element)#adding the specified element to the set
print("The set after adding the elements: ", s)#displays this message after adding the single element 
#adding multiple elements to the set
s1 = set(input("enter your set elements: ").split())#creating set to add multiple elements to the set s
print("The sets after adding the elements: ", s.union(s1))#displays this message after adding the multiple element