'''A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is 
input through the keyboard in hundreds, find the total number of currency notes of each denomination the 
cashier will have to give to the withdrawer'''

amount=int(input("enter the amount"))
hundred=amount//100
amount=amount%100
fifty=amount//50
amount=amount%50
ten=amount//10
print("number of hundreds:",hundred)
print("number of fiftys:",fifty)
print("number of tens:",ten)

'''Output
enter the amount230
number of hundreds: 2
number of fiftys: 0
number of tens: 3'''