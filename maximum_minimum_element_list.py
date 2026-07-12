#finding maximum element in the list name``
name = list(map(int, input("enter your list elements: ").split()))#creating a list from user input
if len(name) == 0:#checking if the list is empty or not
    print("list is empty")#displaying message if list is empty
else:
    name.sort(reverse=True)#arranging all elements in the name in descending order
    print("maximum element in the name: ", name[0])#displaying maximum element
    #finding minimum element in the list name
    name.sort()#arranging all elements in the ascending order
    print("minimum element in the name: ", name[0])#displaying minimum element

