'''The length & breadth of a rectangle and radius of a circle are input through the keyboard.
 Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle.'''

l=int(input("Enter the length of rectangle"))
b=int(input("Enter the breadth of rectangle"))
area=l*b
print("Area:",area)
perimeter=2*(l+b)
print("Perimeter:",perimeter)

'''output
Enter the length of rectangle 4
Enter the breadth of rectangle 2
Area: 8
Perimeter: 12'''
