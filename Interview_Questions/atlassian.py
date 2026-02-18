

# CostExplorer ->
#   monthlyCostList(): Array/List of size 12 filled with cost incurred in each month of the unit year
#   annualCost(): Total cost in a unit year

# annualCost(Customer) float




# Unit year - refers to a calculation unit of year here, it can be Jan-Dec, Apr-Mar, July-June anything that candidate decides as a unit.
# monthlyCostList is an array of size 12

# //  Atlassian pricing plans as tuple of {planId, monthlyCost}
# [
#   {BASIC, 9.99},
#   {STANDARD, 49.99}, 
#   {PREMIUM, 249.99}
# ]

# //  Customer subscription information
# Customer -> C1
# Product -> 
#     Name -> Jira
#     Subscription -> [ BASIC, "2022-03-10”  ] //  { planId, startDate }, date in YYYY-MM-DD format

# 2022-12-01
# [0,0,0,0,0,0,0,0,0,0,0, 9.99]
# 9.99

# [2022-12-01, 2022-12-31]

from enum import Enum
from datetime import datetime
import calendar 

class PricingPlans(Enum):
    BASIC = 9.99
    STANDARD = 49.99
    PREMIUM = 249.99

class Customer():
    def __init__(self, customer_id, product_name, subscription):
        self.customer_id = customer_id
        self.product_name = product_name
        self.subscription_price = PricingPlans[subscription[0]]
        self.susbscription_start_date = subscription[1]
        

class CostExplorer:
    def __init__(self):
        self.total_months = 12
        
    def create_datetime_obj_for_customer(self, date_string):
        format_string = "%Y-%m-%d"
        return datetime.strptime(date_string, format_string)
        
    def find_num_days_for_cur_month(self, date_string):
        datetime_object = self.create_datetime_obj_for_customer(date_string)
        num_days, _= self.get_num_days_in_cur_month(date_string)
        
        last_day_of_month = datetime_object
        last_day_of_month = last_day_of_month.replace(day=num_days)
        
        return (last_day_of_month - datetime_object).days + 1
        
    def get_num_days_in_cur_month(self, date_string):
        dt_obj = self.create_datetime_obj_for_customer(date_string)
        year = dt_obj.year
        month = dt_obj.month
        
        _, num_days = calendar.monthrange(year, month)
        
        return num_days, month
        
    
    def monthlyCostList(self, customer):
        monthly_cost = [0 for i in range(self.total_months)]
        cur_days_for_cur_month = self.find_num_days_for_cur_month(customer.susbscription_start_date)
        num_days, cur_month = self.get_num_days_in_cur_month(customer.susbscription_start_date)
        price_for_current_month = round(cur_days_for_cur_month /(num_days) * customer.subscription_price.value, 2)
        
        monthly_cost[cur_month-1] = price_for_current_month
        
        while cur_month < 12:
            monthly_cost[cur_month] = customer.subscription_price.value
            cur_month += 1
             
        return monthly_cost
    
    def annualCost(self, customer):
        return sum(self.monthlyCostList(customer))
    
customer1 = Customer("C1", "Jira", ["BASIC", "2022-05-31"])
cost_explorer = CostExplorer()

# print(cost_explorer.monthlyCostList(customer1))
# print(cost_explorer.annualCost(customer1))
    
    
    
    
    
    
    
    
    
    
    
    