'''
Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
'''
# Get two integers from the user
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Compare the integers and display the relationship
if a == b:
    print(f"{a} is equal to {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} is greater than {b}.")
'''
Enter the first integer (a): 9
Enter the second integer (b): 12
9 is less than 12.
