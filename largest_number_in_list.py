#find the largest number in a list
def is_largest(name):
    largest_number = name[0]
    for i in range(len(name)):
        if name[i] > largest_number:
            largest_number = name[i]
    return largest_number
name = list(map(int, input("enter your list elements: ").split()))
print(is_largest(name)) 