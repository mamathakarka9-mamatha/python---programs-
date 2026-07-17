#remove and return a random element using built-in pop() method 
s = set(input("Enter your set elements: ").split())#creating a set from user input
if len(s) == 0:#checking if the set is empty
    print("Set is empty after removing the random element.")#confirming that the set is empty
else:
    result = s.pop()#removing and returning a random element from the set
    print("Set after removing a random element:", s)#displaying the set after removing the random element
    print("Random element removed:", result)#displaying the random element that was removed 