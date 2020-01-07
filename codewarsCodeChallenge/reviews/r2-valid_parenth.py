# 1/7/20 9:34 valid parenthesis 
# Review 2

# 9:46
# Personal Test Attempt 1 Success
# Personal Test Attempt 2 Success
# 9:55 21 Minutes
# codewars Success


# Requirements:
#   Given a string, determine if the string is has all valid parenthesis
#   It can contain other characters
#   It can be empty or have no parenthesis
# I/O:
#   ["()", ")(", "", "hello", "(hello)", "(())", "()()", "h)ello()"]
# Process:
#   Iterate through the string
#   Keep a counter to track the number of open parenthesis
#   if the counter is not 0 at the end, return False
#   if the character is ), but counter is 0 return False

def valid_parenthesis(s):
    counter = 0
    for c in s:
        if c == '(':
            counter += 1
        if c == ')':
            if counter == 0:
                return False
            counter -= 1
    if counter != 0:
        return False
    return True

tests = ['()', '(()())', ')(', '(hello)', 'h(ell)o', "()", "()()", "(())", ")", "())", "((()", ""]
answers = [True, True, False, True, True,  True, True, True, False, False, False, True]

for test, answer in zip(tests, answers):
    res = valid_parenthesis(test)
    print(res, 'Success: ', res == answer)
    if res != answer:
        print('Expected', answer)

