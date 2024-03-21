'''Write a program to find the reverse of n digit number using While loop'''
num=int(input("Enter the number:"))
i=num
sum=0

while(num>0):
    rem=num%10
    num=num//10
    sum=(sum*10)+rem
print("The original number is",i)
print("The reverse number is",sum)

'''output
The original number is 345
The reverse number is 543'''