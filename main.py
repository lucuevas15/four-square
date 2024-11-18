"""
This program calculates employees productivity bonus
 and prints employee name and bonus.
"""

#Variable inputs for employee/ transaction history created
employeeName = input("please enter Employee Name: ")
numShifts = float(input("please enter number of shifts: "))
numTrans = float(input("please enter number of transactions: "))
transValue = float(input("please enter transaction value: "))


# # Productivity score calculator
prodScore = (transValue / numTrans / numShifts)


# Bonus if statements
if prodScore <= 30 : bonus = 50.00

elif 31 <= prodScore <= 60 : bonus = 75.00

elif 70<= prodScore <= 199 : bonus = 100.00

elif prodScore >= 200 : bonus = 200.00


# Output Employee Name and Bonus.
print("Employee Name: " + str(employeeName))
print("Employee Bonus: $" + str(bonus)) # type: ignore
