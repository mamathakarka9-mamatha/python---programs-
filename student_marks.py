# This program is used to calculate the percentage of marks obtained by a student and print the corresponding grade based on the percentage.
totalmarks = float(input("Enter your total marks here: "))#the total marks of the student is taken as input from the user
marks = float(input("Enter your marks here: "))#the marks obtained by the student is taken as input from the user
if marks> totalmarks:#checking if the marks obtained by the student is less than or equal to the total marks
 print("Marks cannot be greater than total marks")#displaying an error message if the marks obtained by the student is greater than the total marks
elif totalmarks <= 0:#checking if the total marks is less than or equal to zero
    print("Total marks cannot be zero or negative")#displaying an error message if the total marks is less than or equal to zero
elif marks < 0:#checking if the marks obtained by the student is less than zero
    print("Marks cannot be negative")#displaying an error message if the marks is less than zero
elif (marks/totalmarks)*100 >= 90:#checking if the percentage of marks obtained by the student is greater than or equal to 90
    print("Outstanding")#displaying the grade "Outstanding" if the percentage is greater than or equal to 90
elif (marks/totalmarks)*100 < 90 and (marks/totalmarks)*100 >= 80:#checking if the percentage of marks obtained by the student is less than 90 but greater than or equal to 80
    print("Excellent")#displaying the grade "Excellent" if the percentage is less than 90 but greater than or equal to 80
elif (marks/totalmarks)*100<80 and (marks/totalmarks)*100 >= 70:#checking if the percentage of marks obtained by the student is less than 80 but greater than or equal to 70
    print("Very Good")#displaying the grade "Very Good" if the percentage is less than 80 but greater than or equal to 70
elif (marks/totalmarks)*100< 70 and (marks/totalmarks)*100 >= 60:#checking if the percentage of marks obtained by the student is less than 70 but greater than or equal to 60
    print("Good")#displaying the grade "Good" if the percentage is less than 70 but greater than or equal to 60
elif (marks/totalmarks)*100 < 60 and (marks/totalmarks)*100 >= 50:#checking if the percentage of marks obtained by the student is less than 60 but greater than or equal to 50
    print("Average")#displaying the grade "Average" if the percentage is less than 60 but greater than or equal to 50
elif (marks/totalmarks)*100<50 and (marks/totalmarks)*100 >= 40:#checking if the percentage of marks obtained by the student is less than 50 but greater than or equal to 40
    print("Pass")#displaying the grade "Pass" if the percentage is less than 50 but greater than or equal to 40
elif (marks/totalmarks)*100<40:#checking if the percentage of marks obtained by the student is less than 40
    print("Fail")#displaying the grade "Fail" if the percentage is less than 40
else:
    print("Absent")#displaying the grade "Absent" if the student is absent