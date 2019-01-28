# Author Maina Wanjau

import math
#class for checking payment period in years based on annual salary savings
class paymentyears:
    def __init__(self):
        self.total_cost=0           #total cost of the house
        self.annual_salary= 0.0     #Annual salary
        self.portion_saved=0.0      #% of salary saved of salary

    def getDetails(self):
        self.annual_salary = float(input("Input your annual Salary: "))
        self.portion_saved = float(input("Input your monthly salary portion to be saved: as a % "))
        self.total_cost = float(input("What is the cost of your dream house ? "))
        self.portion_saved = self.portion_saved/100         #convert user input to decimal
        self.computeAnnualSavings()     # call the cannual savings computing function

    def computeAnnualSavings(self):
        self.annual_savings= self.portion_saved*self.annual_salary      #compute anual savings
        print("Annual savings has been calculated")
        self.computeYearsOfPayment()
    
    def computeYearsOfPayment(self):
        house = self.total_cost
        self.payment_duration = house/self.annual_savings       #compute number of years
        years =round(self.payment_duration,2)       # round off the value to 2 decimal places
        yrs = str(years)            #convert variable to string
        years_month = yrs.split('.')        #first portion to be years and the other to be months
        months = int(years_month[1])/100*12     # compute the months
        print(" It will take {0} years and {1} months to pay for your house ".format(years_month[0],months,))
               
a= paymentyears()  #instanciate class object
a.getDetails()





