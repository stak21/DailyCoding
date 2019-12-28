# 12/28/19 10:18 AM

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

