'''A library charges a fine for every book returned late.
 For first 5 days the fine is 50 paise, for 6-10 days fine is one rupee and above 10 days fine is 5 rupees.
   If you return the book after 30 days your membership will be cancelled.
     Write a program to accept the number of days the member is late to return the book and display the fine or the appropriate message.
'''
days=int(input("Enter the number of days: "))
if (days>0 and days<=5):
    fine=days*0.5
    print("Amount to pay = Rs:",fine)

elif (days>=6 and days<=10):
     fine=days*1
     print("Amount to pay = Rs:",fine)
elif (days>10 and days<=30):
     fine=days*5
     print("Amount to pay = Rs:",fine)
else:
    print("Membership cancelled")

    '''output
    Enter the number of days: 35
Membership cancelled'''
