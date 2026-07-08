#checking whether a given year is leap year or non-leap year
year = int(input("enter the year: ")) #using type casting and converting string into integer
if year%100==0 and year%400==0 and year%4==0:
    print("given year is a leap year")
elif year%4==0 and year%400!=0 and year%100!=0:
    print("it's a leap year")
elif year%4==0 and year%100==0 and year%400!=0:
    print("it's a non-leap year")
elif year%4!=0:
    print("it's not a leap year")