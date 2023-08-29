#program to check if the given year is leap year or not


year=int(input("Enter any year : "))
if ((year % 400==0) or
     (year%100!=0) and 
     (year%4==0)):
    print("Given year is leap year")
else:
    print("Given year is not leap year")
