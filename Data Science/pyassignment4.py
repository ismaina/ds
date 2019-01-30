# Author Maina Wanjau
class HouseHunting:

    def __init__(self):
        self.total_cost = 100000000
        self.portion_down_payment = 0
        self.current_savings = 0
        self.monthly_rate = 0.04
        self.annual_salary=0
        self.saved_portion = 0.1
        self.monthly_salary = 0
        self.number_of_months = 0
        self.semi_annual_raise = 0.0704
        self.monthly_savings = 0.0
        self.guesses = 0.0
        self.low = 0.0
        self.high = 1.0
        self.bs= (self.high + self.low) / 2.0

        self.getDetails()


    def getDetails(self):
        self.annual_salary = float(input("Enter your annual salary: "))
        self.saved_portion = float(input("Enter the portion of salary to be saved: "))
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
            for self.number_of_months in range(1,37):

                if self.number_of_months % 6 == 0:
                    self.annual_salary += self.annual_salary * self.semi_annual_raise
                    self.monthly_savings = (self.annual_salary/12) * self.saved_portion

                self.current_savings += self.monthly_savings

                
                print(str(self.number_of_months),"\t",str(self.current_savings),"    ", str(self.annual_salary))
            
            print('You will need to save up for {0} months to pay for the deposit'.format(self.number_of_months))

            if self.annual_salary < self.portion_down_payment - 100:
                print('Its is not possible to pay the down payment in three years')
            else:
                self.current_savings = self.annual_salary * self.bs
                while abs(self.current_savings - self.portion_down_payment) >= 100.0:
                    self.guesses += 1
                    if self.current_savings < self.portion_down_payment:
                        self.low = self.bs
                    else:
                        self.high = self.bs
                    self.bs = (self.high + self.low) / 2.0
                    self.current_savings = self.annual_salary * self.bs
                print(' The best savings rate: {0}'.format(self.bs))
                print(" Steps in bisection search :", self.guesses)

        #print('You will need to save up for {0} months to pay for the deposit'.format(self.number_of_months))
a = HouseHunting() #call the class object