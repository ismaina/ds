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
        self.monthly_savings = 0.0

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
        self.monthly_savings = (self.annual_salary/12) * self.saved_portion

        print(self.portion_down_payment)
        print('month \t current saings \t annual salary')
        while self.current_savings <= self.portion_down_payment:
            self.current_savings += self.monthly_savings
            self.number_of_months += 1

            if self.number_of_months % 6 == 0:
                self.annual_salary += self.annual_salary * self.semi_annual_raise
                self.monthly_savings = (self.annual_salary/12) * self.saved_portion

            self.current_savings += self.monthly_savings

            
            print(str(self.number_of_months),"\t",str(self.current_savings),"    ", str(self.annual_salary))
        
        print('You will need to save up for {0} months to pay for the deposit'.format(self.number_of_months))


a = HouseHunting()
