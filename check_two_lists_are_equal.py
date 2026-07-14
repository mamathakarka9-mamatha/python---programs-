#checking two lists are equal or not 
lst1 = list(map(int, input("Enter your list1 elements: ").split()))#creating list1 from user input
lst2 = list(map(int, input("Enter your list2 elements: ").split()))#creating list2 from user input
if lst1 == lst2:#checking if two lists are equal
    print("given two lists are equal")#displaying this message if two lists are equal
else:
    print("given two lists are not equal") #displaying this message if two lists are not equal
