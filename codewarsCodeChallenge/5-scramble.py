# 1/7/20 11:00 PM scramble

# 11:06 - Prep finished
# 11:11 - Finished attempt
# Test phase 
# 11:15PM PTA Success
# 11:20 PM codewars attempt Failed. Took too long

# Ideas - Search for the characters in str 2 while creating the mappings

# Requirements:
#   Given 2 strings, return true if the letters of one string can creat the second string
#       punctuations and digits will not be included
# I/O:
#   ('ahello', 'hello'),  ('ahell', 'hello'), ('heal', 'a')
#   True, False, True
# Process:
#   Create a mapping of all the letters from str1
#       Iterate through str1 as c
#           if c in dictionary:
#               increment value
#           else create entry
#   itertate through str2 and if any characters are not in the dictionary, return False
#  if mapping count == 0
#      remove it

def scramble(str1, str2):
    mappings = {}

    if len(str1) < len(str2):
        return False
    for c in str1:
        if c in mappings:
            mappings[c] += 1
        else:
            mappings[c] = 1
    for c in str2:
        if c not in mappings:
            return False
        mappings[c] -= 1
        if mappings[c] == 0:
            mappings.pop(c)
    return True

tests = [ ('ahello', 'hello'),  ('ahell', 'hello'), ('heal', 'a')]
answers = [True, False, True]

for test, answer in zip(tests, answers):
    res = scramble(test[0], test[1])
    print(res, 'Success: ', res == answer)
    if res != answer:
        print('Expected', answer)