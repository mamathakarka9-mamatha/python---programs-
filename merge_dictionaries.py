#merging dictionary1 and dictionary2 into a new dictionary 
n = int(input("enter the number of elements in dictionary1: "))#number of elements in dictionary1
dictionary = {}#creating empty dictionary to merge dictionary1 and dictionary2
dictionary1 = {}#creating empty dictionary1
dictionary2 = {}#creating empty dictionary2
for i in range(n):#loop to input elements in dictionary 1
  keyi = input("enter your key: ")#key input
  valuei = int(input("enter your value: "))#value input
  dictionary[keyi] = valuei#adding dictionary1 elements to dictionary
  a = {keyi: valuei}#creating dictionary1 with key and value
  dictionary1.update(a)#updating the main dictionary1 with new key-value pair
print("Before merging dictionary: ", dictionary1)#displaying the final dictionary1
n1 = int(input("enter the number of elements in dictionary2: "))#number of elements in dictionary2
for j in range(n1):##loop to input elements in dictionary2
  keyj = input("enter your key: ")#key input
  valuej = int(input("enter your value: "))#value input
  dictionary[keyj] = valuej#adding dictionary2 elements to dictionary
  b = {keyj: valuej}#creating dictionary2 with key and value
  dictionary2.update(b)#updating the main dictionary2 with new key-value pair
print("Before merging dictionary: ", dictionary2)#displaying the final dictionary2
print("After merging dictionary1 and dictionary2: ", dictionary)#dictionary after merging dictionary1 and dictionary2 