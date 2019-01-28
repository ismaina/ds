annual_salary = int(input("Salary: "))
portion_saved = float(input("Percentage to save: ")) 
total_cost = int(input("Cost of the house: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
rate = 0.04
number_of_months = 0
semi_annual_raise = float(input("Raise: "))

while current_savings <= portion_down_payment:
    current_savings += annual_salary * portion_saved / 12
    current_savings += current_savings * rate / 12
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    print(number_of_months, current_savings)

print("Enter your annual salary: ", annual_salary)  
print("Enter the percent of your salary to save, as a decimal: ", portion_saved)
print("Enter the cost of your dream home: ", total_cost) 
print("Number of months: ", number_of_months)    