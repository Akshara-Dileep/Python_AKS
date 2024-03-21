'''Two numbers are input through the keyboard into two locations C and D.
 Write a program to interchange the contents of C and D.

'''
C=int(input("Enter the value of C:"))
D=int(input("Enter the value of D:"))
temp=C
C=D
D=temp
print("C",C)
print("D",D)

'''output
Enter the value of C:4
Enter the value of D:5
C 5
D 4'''