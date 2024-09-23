'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
'''
# Get input for seating capacities of the three labs and the allocated lab
a = int(input("Enter the seating capacity of Lab L1: "))
b = int(input("Enter the seating capacity of Lab L2: "))
c = int(input("Enter the seating capacity of Lab L3: "))
allocated_lab = input("Enter the lab allocated for ACE training (L1, L2, L3): ").strip().upper()

# Initialize a dictionary to hold lab capacities
labs = {
    "L1": a,
    "L2": b,
    "L3": c
}

# Remove the allocated lab from consideration
if allocated_lab in labs:
    del labs[allocated_lab]

# Find the lab with the minimal seating capacity among the remaining labs
min_lab = min(labs, key=labs.get)
min_capacity = labs[min_lab]

# Output the result
print(f"The lab with minimal seating capacity among the available labs is {min_lab} with a capacity of {min_capacity}.")
'''
Enter the seating capacity of Lab L1: 30
Enter the seating capacity of Lab L2: 25
Enter the seating capacity of Lab L3: 40
Enter the lab allocated for ACE training (L1, L2, L3): L1
The lab with minimal seating capacity among the available labs is L2 with a capacity of 25.
