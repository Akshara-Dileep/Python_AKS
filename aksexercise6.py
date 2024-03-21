'''Any year is entered through the keyboard, write a program to determine whether the year is leap or not.
 Use the logical operators && and ||.
'''
year=int(input("Enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
 print(year,"is a leap year")
else:
 print(year,"is not a leap year")
 
'''output
Enter the year:2024
2024 is a leap year'''