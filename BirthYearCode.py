'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
'''
birth_year_last_two = int(input("Enter the last two digits of your birth year (e.g., '62' for 1962): "))
current_year_last_two = int(input("Enter the last two digits of the current year (e.g., '99' for 1999): "))
if birth_year_last_two > current_year_last_two:
    # Assume the birth year is in the 1900s
    birth_year = 1900 + birth_year_last_two
else:
    # Assume the birth year is in the 2000s
    birth_year = 2000 + birth_year_last_two
current_year = 2000 + current_year_last_two
# Calculate age
age = current_year - birth_year
# Output the age
print(f"Your current age is: {age} years")
'''
Enter the last two digits of your birth year (e.g., '62' for 1962): 62
Enter the last two digits of the current year (e.g., '99' for 1999): 99
Your current age is: 37 years
