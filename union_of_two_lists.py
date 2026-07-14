#union of two lists 
lst1 = list(map(int, input("Enter your list1 elements: ").split()))#creating list1 from user input
lst2 = list(map(int, input("Enter your list2 elements: ").split()))#creating list2 from user input
lst1.extend(lst2)#extending list1 with elements from list2
print("union of lst1 and lst2:", lst1)#displaying the union of lst1 and lst2 