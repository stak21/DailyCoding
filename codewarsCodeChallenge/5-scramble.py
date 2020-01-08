# 1/7/20 11:00 PM scramble

# 11:06 - Prep finished
# 11:11 - Finished attempt
# Test phase 
# 11:15PM PTA Success
# 11:20 PM codewars attempt Failed. Took too long
# 11:26 PM Attempt 2
# 11:28 PM PTA2 Success
# 11:35 PM codewars attempt Failed. Took too long

# Ideas - Search for the characters in str 2 while creating the mappings
# ideas - sort both strings
#       start from the last character of str 2
#       check the last chracter of str 1 and if str 1 is < str 2 return False
#       create a binary search function
#       takes in a character and a string,
#           checks the middle of the string 
#               if the character is smaller than the middle
#                   check the shorter side
#       return the index of the found string
#       if not found, return False
#      if found, cut the index of str1 to the returned index
#   
#       

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
    def bsearch(c, string):
        middle = len(string) // 2
        if middle == 0 and c != string[middle]:
            return False
        if c == string[middle]:
            return middle
        if c < string[middle]:
            return bsearch(c, string[:middle])
        else:
            return bsearch(c, string[middle:])
    idx = 0
    sorted_s1 = sorted(str1)
    for c in sorted(str2):
        idx = bsearch(c, sorted_s1)
        print('idx: ', idx)
        if not idx:
            return False
    return True
            


tests = [ ('ahello', 'hello'),  ('ahell', 'hello'), ('heal', 'a')]
answers = [True, False, True]

for test, answer in zip(tests, answers):
    res = scramble(test[0], test[1])
    print(res, 'Success: ', res == answer)
    if res != answer:
        print('Expected', answer)