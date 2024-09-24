'''
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
'''
x = int(input("Enter capacity of L1: "))
y = int(input("Enter capacity of L2: "))
z = int(input("Enter capacity of L3: "))
n = int(input("Enter number of students: "))
feasible_labs = []
if x >= n:
    feasible_labs.append((x, "L1"))
if y >= n:
    feasible_labs.append((y, "L2"))
if z >= n:
    feasible_labs.append((z, "L3"))
if not feasible_labs:
    print("No lab can accommodate the students.")
else:
    chosen_lab = max(feasible_labs, key=lambda lab: lab[0])
    print(f"Allocate lab: {chosen_lab[1]}")

'''
Enter capacity of L1: 30
Enter capacity of L2: 40
Enter capacity of L3: 20
Enter number of students: 25
Allocate lab: L2
​
