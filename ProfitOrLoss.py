'''
 A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
'''
total_cost = float(input("Enter the total cost for a dozen bananas (X): "))
selling_price_per_banana = float(input("Enter the selling price per banana (Y): "))
total_selling_price = selling_price_per_banana * 12
profit_or_loss = total_selling_price - total_cost
if profit_or_loss > 0:
    print(f"Profit of Rs.{profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss of Rs.{abs(profit_or_loss):.2f}")
else:
    print("No Profit No Loss")
'''
Enter the total cost for a dozen bananas (X): 120.0
Enter the selling price per banana (Y): 10.0
Loss of Rs.0.00
