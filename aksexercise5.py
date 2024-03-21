'''If the ages of Ram, Shyam and Ajay are input through the keyboard,
 write a program to determine the youngest of the three.

'''
A1=int(input("enter Ram's age:"))
A2=int(input("Enter Shyam's age:"))
A3=int(input("Enter Ajay's age:"))
if A1<A2 and A1<A3:
 print("Ram is youngest")
elif A2<A1 and A2<A3:
 print("Shyam is youngest")
else :
 print("Ajay is the youngest")
 
 '''output
 enter Ram's age:35
Enter Shyam's age:25
Enter Ajay's age:10
Ajay is the youngest'''