#remove an element using remove()
s = set(input("Enter your set elements: ").split())#taking input from the user
element = input("Enter your element for deletion: ")#enter your element for the deletion
s.remove(element)#entering the element for deletion 
print("set s after deleting the element from the set: ", s)#displays this message after deletion