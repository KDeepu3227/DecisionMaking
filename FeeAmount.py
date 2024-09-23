'''
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS
Tuition fee + Bus fee
Merit Seat Hosteller
MSH
Tuition fee + Hostel fee
Management Seat Day Scholar
MGSDS
150% of Tuition fee + Bus fee
Management Seat Hosteller
MGSH
150% of Tuition fee + Hostel fee
Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
'''
student_type = input("Enter the student type (MSDS, MSH, MGSDS, MGSH): ").strip().upper()
tuition_fee = float(input("Enter the tuition fee: "))
additional_fee = float(input("Enter the bus fee or hostel fee: "))
fee_amount = 0
if student_type == "MSDS":
    fee_amount = tuition_fee + additional_fee  # Tuition fee + Bus fee
elif student_type == "MSH":
    fee_amount = tuition_fee + additional_fee  # Tuition fee + Hostel fee
elif student_type == "MGSDS":
    fee_amount = 1.5 * tuition_fee + additional_fee  # 150% of Tuition fee + Bus fee
elif student_type == "MGSH":
    fee_amount = 1.5 * tuition_fee + additional_fee  # 150% of Tuition fee + Hostel fee
else:
    print("Invalid student type entered.")
    exit()
print(f"The total fee amount to be collected is: Rs.{fee_amount:.2f}")
'''
Enter the student type (MSDS, MSH, MGSDS, MGSH): MSDS
Enter the tuition fee: 20000
Enter the bus fee or hostel fee: 5000
The total fee amount to be collected is: Rs.25000.00
