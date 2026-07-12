#adding key value pair to dictionary
n= int(input("enter the number of elements in dictionary: "))#number of elements in dictionary
dictionary = {}#creating empty dictionary
for i in range(n):#loop to input elements
  keyi = input("enter your keyi: ")#key input
  valuei = int(input("enter your valuei: "))#value input
  a = {keyi: valuei}#creating dictionary with key and value
  dictionary.update(a)#updating the main dictionary with new key-value pair
print(dictionary)#displaying the final dictionary
n1 = int(input("enter how many pairs you need to add: "))
for j in range(n1):
 keyj = input("enter your key to add: ")
 valuej = int(input("enter your value to add: "))
 dictionary[keyj] = valuej
print(dictionary)