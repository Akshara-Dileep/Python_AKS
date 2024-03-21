'''If a five-digit number is input through the keyboard, write a program to reverse the number.

'''

original_number = int(input("Enter Number:"))
def reverse_num(num):

    num_str=str(num)
    reverse_str=num_str[::-1]
    reverse_num=int(reverse_str)
    return reverse_num


reversed_result = reverse_num(original_number)
print(f"Original number: {original_number}")
print(f"Reversed number: {reversed_result}")

'''output
Enter Number:234
Original number: 234
Reversed number: 432'''