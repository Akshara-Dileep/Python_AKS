'''write a Python program to check a list is empty or not
'''
def list(list1):
 return len(list1)==0
list1=[1,2,3,4]
if len(list1) == 0:
    print("List is empty.")
else:
    print("List isn't empty.")
    
'''output
List isn't empty.'''