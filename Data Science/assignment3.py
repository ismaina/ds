# Author Maina Wanjau

import math
#class for checking payment period in years based on annual salary savings
class paymentyears:
    def __init__(self):
        self.total_cost=0           #total cost of the house
        self.annual_salary= 0.0     #Annual salary
        self.portion_saved=0.0      #% of salary saved of salary
        self.semi_annual_raise = 0.0
        self.investments = 0.0
        self.years_without_increment =0.0
        self.down_payment = 0.0
        self.rate = 0.04
        self.number_of_months = 0
        self.semi_annual_raise = 0.0
        self.current_savings = 0.0

    def getDetails(self):
        self.annual_salary = float(input("Input your annual Salary: "))
        self.portion_saved = float(input("Input your monthly salary portion to be saved: as a % "))
        self.total_cost = float(input("What is the cost of your dream house ? "))
        self.semi_annual_raise = float(input("What is you semi annual raise ? "))
        self.portion_saved = self.portion_saved/100         #convert user input to decimal
        self.computeAnnualSavings()     # call the cannual savings computing function

    def computeAnnualSavings(self):
        self.annual_savings= self.portion_saved*self.annual_salary      #compute anual savings
        print("Annual savings has been calculated")
        self.computeYearsOfPaymentnoIncrement()
    
    def computeYearsOfPaymentnoIncrement(self):
        house = self.total_cost
        self.payment_duration = house/self.annual_savings       #compute number of years
        years =round(self.payment_duration,2)       # round off the value to 2 decimal places
        self.years_without_increment =years           
        yrs = str(years)                            #convert variable to string
        years_month = yrs.split('.')        #first portion to be years and the other to be months
        months = int(years_month[1])/100*12     # compute the months
        print(" It will take {0} years and {1} months to pay for your house  without increment".format(years_month[0],months,))
        self.computeYearsOfPaymentwithInc()


    def computeYearsOfPaymentwithInc(self):
        print("\n\n\n Calculating your how long it will take to pay your house based on you bi annual increment \n\n")
        self.number_of_months = 0
        self.down_payment = self.total_cost * 0.25
        
        print('__________showing monthly incremental savings__________')
        
        while self.current_savings <= self.down_payment:
            self.current_savings += self.annual_salary *  self.portion_saved / 12
            self.current_savings += self.current_savings *  self.rate / 12
            self.number_of_months +=1
            if self.number_of_months % 6 == 0:
                self.annual_salary += self.annual_salary * self.semi_annual_raise
            print(self.number_of_months, self.current_savings)

        print('__________end of monthly incremental savings__________')
        saved_years = self.years_without_increment*12 - float(self.number_of_months)
        saved_years = round(saved_years/12,2)
        print('\n\t\t Summary \n')
        print("Based on your annual salary it will take \n {0} months to pay for your home and \n {1} years saved based on your increment".format( str(self.number_of_months), str(saved_years)))

               
a= paymentyears()  #instanciate class object
a.getDetails()





