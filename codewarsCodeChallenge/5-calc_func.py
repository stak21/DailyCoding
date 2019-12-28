# 12/28/19 10:18 AM

# Fail 11:22 AM
# Requirements: Create a  function for each digit and each mathmatical operation
#   The operation will work on two numbers
#   To call an operation, it must be called by a digit function and the operation will take the inner digit function
#   Return integers
#  I/O:
#   five(plus(three())) => 8
#   five(times(zero())) => 0
#   five(divided_by(six())) => 0
#   five(divided_by(two())) => 2
#   zero(divided_by(five())) => 0
#   five(divided_by(zero())) => error
#  Process:
#   So if the number  is the left operand, then it should expect the operator function
#       It should pass its own number into the function and return the whole thing
#   The operator should expect a number function
#       the operator will call the number function and do the operator on the passed in number and the returned number frmo the number function and return it
#   if the number function is the right operand, then it should not expect anything and return the number

# problem - Most inner function gets called first. Meaning the out function will recieve either a string or a number
#   How do I figure out what the operator is. 
#   if i return a string, then on the first function I can parse through the string and operate on them

def zero(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 0
    
def one(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 1
def two(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 2
    if operator:
        return operator[0](0, operator[1])
    return 3
def four(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 4
def five(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 5
def six(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 6
def seven(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 7
def eight(operator: function = None): #your code here
    if operator:
        return operator[0](0, operator[1])
    return 8
def nine(operator: function = None): #your code here
    if operator:`
        return operator[0](0, operator[1])
    return 9

def plus(operand1: number, operand2: number = None): #your code here
    if  operand2 and isinstance(operand2, int):
        return operand1 + operand2
    return plus, operand 1
def minus(operand1: number, operand2: number = None): #your code here
    if  operand2 and isinstance(operand2, int):
        return operand1 - operand2
    return minus, operand1
def times(operand1: number, operand2: number = None): #your code here
    if  operand2 and isinstance(operand2, int):
        return operand1 * operand2
    return times, operand 1
def divided_by(operand1: number, operand2: number = None): #your code here
    if  operand2 and isinstance(operand2, int):
        if operand2 == 0:
            return 0
        return operand1 / operand2
    return times, operand 1
