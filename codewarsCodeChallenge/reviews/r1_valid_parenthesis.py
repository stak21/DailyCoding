# Requirements:
#   given a string, return True if the parenthesis are valid
#   else False
# Input: 
#   "()"    | True
#   "(())"  | True
#   "()()"  | True
#   "())"   | False
#   ""      | True
#   "(dwa)  | True

# Process:
#   Approach 1:
#       because we are only looking for a parenthesis, we can keep track of the count of parenthesis
#       if the count is 0, return True
#       else False
def valid_parenthesis(string: str) -> bool:
    count = 0
    for c in string:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

tests = ["()", "(())", "()()", "())", "", "(dwa)"]
answers = [True, True, True, False, True, True]
for test, answer in zip(tests, answers):
    res = valid_parenthesis(test)
    print(res, 'Success: ', res == answer)
        
