#finding the second smallest number in the list
def second_smallest(name):#defining the function
    if len(name) <= 1:#checking length of the list
        return "no second smallest number"#returning the message if length is less than or equal to 1
    name.sort()#sorting the list
    for i in range(1, len(name)): #iterating through the list starting from index 1 to second last index
      if name[i] != name[0]:#checking if the current element is not equal to the first element
        return name[i] #returning the second smallest number if found
    return "no second smallest number"#returning the message if no second smallest number is found
name = list(map(int, input("enter your list elements: ").split()))#creating a list of integers from user input
print(second_smallest(name))#displaying the second smallest number in the list