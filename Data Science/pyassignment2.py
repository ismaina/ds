# Author Maina Wanjau
class HouseHunting:

    def __init__(self):
        self.total_cost = 0
        self.portion_down_payment = 0
        self.current_savings = 0
        self.monthly_rate = 0.04
        self.annual_salary=0
        self.saved_portion = 0.1
        self.monthly_salary = 0
        self.number_of_months = 0
        self.semi_annual_raise = 0.1

        self.getDetails()


    def getDetails(self):
        self.annual_salary = float(input("Enter your annual salary: "))
        self.saved_portion = float(input("Enter the portion of salary to be saved: "))
        self.total_cost = float(input("Enter the amount of your dream house: "))
        self.semi_annual_raise = float(input("Enter your bi-annual raise rate : "))
        self.monthly_salary = self.annual_salary/12
        self.portion_down_payment = self.total_cost * 0.04

        self.computesavings()

    def computesavings(self):
        self.number_of_months =0

        while self.current_savings <= self.portion_down_payment:
            self.current_savings += self.monthly_salary * self.saved_portion
            self.current_savings += self.monthly_salary * self.monthly_rate
            self.number_of_months += 1
        
        print('You will need to save up for {0} months to pay for the deposit'.format(self.number_of_months))


a = HouseHunting()
