#remove an element from a set using built-in discard() method
s = set(input("Enter your set elements: ").split())#creating set from user input
element = input("Enter your set element for deletion: ")#enter element for discarding from a set
s.discard(element)#discarding a element
print("set s after the discarding the element: ", s)#displays this message after discarding the element from set 