#finding common elements in a list
def func(lst1, lst2):#defining a function to find common elements in two lists
 common = []#creating empty list to store common elements
 for i in range(len(lst1)):#looping through first list
    for j in range(len(lst2)):#looping through second list
     if lst1[i] == lst2[j]:#checking if elements are equal
      common.append(lst1[i])# appending common elements to the list
 return common#returning the list of common elements
lst1 = list(map(int, input("Enter your list1 elements: ").split()))#creating list1 by taking input from user and converting it to list of integers
lst2 = list(map(int, input("Enter your list2 elements: ").split()))#creating list2 by taking input from user and converting it to list of integers
print(func(lst1, lst2))#printing the common elements in the list 