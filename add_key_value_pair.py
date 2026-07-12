#add key-value pair to dictionary
n=int(input("enter the number of elements in dictionary: "))#enter the number of elements in dictionary 
dictionary = {}#creating empty dictionary
for i in range(n):#loop to input elements
    keyi = input("enter your keyi: ")#key input
    valuei = int(input("enter your valuei: "))#value input
    dictionary.update({keyi: valuei})#updating the dictionary with key-value pair
print("before updating dictionary: ", dictionary)#displaying dictionary before updating 
dictionary.update({'num':12345, 'abc':12})#updating dictionary with new key-value pair
print("after updating dictionary: ", dictionary)#displaying dictionary  after updating