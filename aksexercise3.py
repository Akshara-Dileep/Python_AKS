'''While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. 
If quantity and price per item are input
through the keyboard, write a program to calculate the total expenses.'''

quantity=int(input("Enter the quantity") )
price=int(input("Enter the price per item"))
total=quantity*price
if quantity>10:
    total=total-(total*0.1)
else:
    total=quantity*price
print("Total expences=",total)       

'''output
Enter the quantity5
Enter the price per item 2
Total expences= 10'''