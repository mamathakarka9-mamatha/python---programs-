#checking whether a list has duplicates or not
def has_duplicates(name):#defining the function
    for i in range(len(name)):#iterating through a list
        for j in range(i+1, len(name)):#iterating through a list
            if name[i] == name[j]:#checking for the common elements
                return True#if condition executes return true
    return False#if condition doesn't executes return false
name = list(map(int, input("enter your list elements: ").split()))#creating a list from user input
print(has_duplicates(name))#displaying the output has true or false