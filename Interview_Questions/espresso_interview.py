"""

Implent a basic calculator
- plus, minus, multipliaction and division
- input is provided as a string with no spaces
- honor BEDMAS
- output the calculated value
- always a valid expression


Given an input
    - do a split on multiplication
        - an array of value that need to be multiplied
        - iterate over this array and check each for any division
            - 

"""

from enum import Enum
class Operation(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

# [2+2x2+2]
# [2+2, 2+2] Multiply

def compute_expression(expression):
    
    operations = [Operation.PLUS.value, Operation.MINUS.value, Operation.MULTIPLY.value, Operation.DIVIDE.value]
    value = None

    for item in expression:
        for operation in operations:
            if operation in item:
                split = item.split(operation)
                for exp in split:
                    if check_includes_any_operation(exp):
                        compute_value = compute_expression([exp])
                    else:
                        compute_value = int(exp)

                    if value == None:
                        value = compute_value
                        continue
                    
                    if operation == Operation.MULTIPLY.value:
                        value *= compute_value
                    elif operation == Operation.DIVIDE.value:
                        value /= compute_value
                    elif operation == Operation.PLUS.value:
                        value += compute_value
                    elif operation == Operation.MINUS.value:
                        value -= compute_value
                break

    return value

def check_includes_any_operation(exp):
    operations = [Operation.MULTIPLY.value, Operation.DIVIDE.value, Operation.PLUS.value, Operation.MINUS.value]

    for operation in operations:
        if operation in exp:
            return True
    return False

print(compute_expression(['2+2*2-10']))