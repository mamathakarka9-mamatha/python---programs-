def total_list(name):#defining the function
    total = 0 #initially we are taking total as 0
    for i in range (len(name)):#iterating through the list
      total = total + name[i] #adding the elements of the list
    return total #returning the total of the list
name = list(map(int, input("Enter the list elements: ").split()))#creating a list of integers from user input
print(total_list(name))#displaying the total of the list
    