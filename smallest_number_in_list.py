#finding smallest number in a list
def is_smallest(name):#defining a function to find the smallest number in a list
    smallest_number = name[0]#considering the first element of the list as the smallest number
    for i in range(len(name)):#iterating through the list
        if name[i]<smallest_number:#checking if the current element is smaller than the smallest number
            smallest_number = name[i]#modifying the smallest number if the current element is smallest
    return smallest_number#returning the smallest number after iterating through the list
name = list(map(int, input("enter your list elements: ").split()))#creating a list of integers from user input
print(is_smallest(name))#displaying the smallest number in the list