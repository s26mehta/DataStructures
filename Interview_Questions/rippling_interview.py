"""
We plan to offer a corporate credit card to companies that employees can use for business expenses.
Managers can set policies on the cards so that employees do not misuse the card or exceed allowances.
We're going to be building the rules engine that supports this product.
You are encouraged to ask product-oriented questions and to share your assumptions.

We will start with some very basic rules:

* No expense at a restaurant can exceed $75 ("vendor_type" == "restaurant")
* No airfare expenses ("expense_type" == "airfare")
* No entertainment expenses ("expense_type" == "entertainment")
* No expenses over $250
* A trip cannot exceed $2000 in total expenses
* Total meal expenses cannot exceed $200 per trip

Let's look at an example of an expense:


expenses: list[dict[str, str]] = [
    {
        "expense_id": "001",
        "trip_id": "001",
        "amount_usd": "49.99",
        "expense_type": "client_hosting",
        "vendor_type": "restaurant",
        "vendor_name": "Outback Roadhouse",
    },
]


Let's design a system that can handle these rules and flag expenses and trips that violate them.
Implement the following function:

```
evaluate_rules(rules: list<rule>, expenses: list<expense>) -> ???
```

Expenses will be provided to you as a list of hashmap/dictionary objects with `string` keys and values.

The return type of evaluate_rules is up to you.

In the future, we will add more types of rules and allow rule creation via an API, so we encourage you to think about the flexibility of your design.

Before you get started coding, let's discuss the return function's return type.

"""


class RuleObj:
    def __init__(self, value, comparing_function, comparing_value):
        self.value = value
        self.comparing_function = comparing_function
        self.comparing_value = comparing_value


class Rule:
    def __init__(self, rules_list, description, level="expense"):
        self.rules_list = rules_list
        self.description = description
        self.level = level
    
    def evaluate_rule(self, expense, trip):
        result = True
        check_obj = expense if self.level == "expense" else trip
        if self.level == "expense":
            for rule in self.rules_list:
                if rule.comparing_function(check_obj[rule.value], rule.comparing_value) == False:
                    result = False
        elif self.level == "trip":
            for rule in self.rules_list:
                if rule.comparing_function(check_obj.__getattribute__(rule.value), rule.comparing_value) == False:
                    result = False
        return result
        

class Trip:
    def __init__(self, trip_id):
        self.trip_id = trip_id
        self.total_amount_spent = 0
        self.total_meal_expenses = 0
        self.all_rules_passed = True
        self.rules_failed = []
        self.expenses = []

class Expense:
    def __init__(self, expense_id):
        self.expense_id = expense_id
        self.all_rules_passed = True
        self.rules_failed = []
        
        
        
def evaluate_rules(rules, expenses): # rules: list<rule>, expenses: list<expense>
    trips_dictionary = {}
    
    for expense in expenses:
        trip_id = expense['trip_id']
        if trip_id not in trips_dictionary:
            trips_dictionary[trip_id] = Trip(trip_id)
        
        expenseObj = Expense(expense['expense_id'])
        
        trips_dictionary[trip_id].expenses.append(expenseObj)
        trips_dictionary[trip_id].total_amount_spent += float(expense['amount_usd'])

        if expense["vendor_type"] == "restaurant":
            trips_dictionary[trip_id].total_meal_expenses += float(expense['amount_usd'])

        for rule in rules:
            evaluate_rule = rule.evaluate_rule(expense, trips_dictionary[trip_id])
            obj = expenseObj if rule.level == "expense" else trips_dictionary[trip_id]
            if evaluate_rule == False:
                obj.all_rules_passed = False
                obj.rules_failed.append(rule.description)
    return trips_dictionary

def less_than_comparator(val1, val2):
    if float(val1) < float(val2):
        return True
    return False

def equal_to_comparator(val1, val2):
    if val1 == val2:
        return True
    return False

def not_equal_to_comparator(val1, val2):
    if val1 != val2:
        return True
    return False

rule1_list = [
    RuleObj('amount_usd', less_than_comparator, 75,),
    RuleObj('vendor_type', equal_to_comparator, 'restaurant')
]
rule1 = Rule(rule1_list, "No expense at a restaurant can exceed $75 for vendor_type == resturant")

rule2_list = [
    RuleObj('expense_type', not_equal_to_comparator, 'airfare')
]
rule2 = Rule(rule2_list, "No airfare expenses ('expense_type' == 'airfare')")

rule3_list = [
    RuleObj('expense_type', not_equal_to_comparator, 'entertainment')
]
rule3 = Rule(rule3_list, "No airfare expenses ('expense_type' == 'entertainment')")

rule4_list = [
    RuleObj('amount_usd', less_than_comparator, 250)
]
rule4 = Rule(rule4_list, "No expenses over $250")

rule5_list = [
    RuleObj('total_amount_spent', less_than_comparator, 2000)
]
rule5 = Rule(rule5_list, "A trip cannot exceed $2000 in total expenses", "trip")

rule6_list = [
    RuleObj('total_meal_expenses', less_than_comparator, 200)
]
rule6 = Rule(rule6_list, "Total meal expenses cannot exceed $200 per trip", "trip")

all_rules = [rule1, rule2, rule3, rule4, rule5, rule6]

expenses: list[dict[str, str]] = [
    {
        "expense_id": "001",
        "trip_id": "001",
        "amount_usd": "49.99",
        "expense_type": "client_hosting",
        "vendor_type": "restaurant",
        "vendor_name": "Outback Roadhouse",
    },
    {
        "expense_id": "001",
        "trip_id": "002",
        "amount_usd": "49.99",
        "expense_type": "client_hosting",
        "vendor_type": "restaurant",
        "vendor_name": "Outback Roadhouse",
    },
    {
        "expense_id": "002",
        "trip_id": "001",
        "amount_usd": "300.99",
        "expense_type": "client_hosting",
        "vendor_type": "restaurant",
        "vendor_name": "Outback Roadhouse",
    },
]

result = evaluate_rules(all_rules, expenses)
for key, value in result.items():
    print("Trip: [" + key + "],  Trip passes all rules: [" + str(value.all_rules_passed) + "], Trip failed rules: [" + ", ".join(value.rules_failed) + "]")
    for expense in value.expenses:
        print("-- Expense: [" + expense.expense_id + "],  Expense passes all rules: [" + str(expense.all_rules_passed) + "], Expense failed rules: [" + ", ".join(expense.rules_failed) + "]")