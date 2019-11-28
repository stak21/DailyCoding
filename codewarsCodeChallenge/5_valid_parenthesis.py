# Requirements:
#   parenthesis only
#   return true if the string is a valid parenthesis
#   else false
#   Ex: ((())) True
#       ())( False
#   Input: ()()(()())
#   Process:
#       Approach one: Use a dictionary and a stack. For each open, there should be a closed in the stack.
#       Approach two: because we are only looking for a parenthesis, we can keep a count. 
#   Output: True

def valid_parenthesis(s: str) -> bool:
    count = 0
    for c in s:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
            if count < 0:
                return False
    if count != 0:
        return False
    return True

tests = ["()", "()()", "(())", ")", "())", "((()", ""]
answers = [True, True, True, False, False, False, True]

for test, answer in zip(tests, answers):
    res = valid_parenthesis(test)
    print('result: {}'.format(res), res == answer)
