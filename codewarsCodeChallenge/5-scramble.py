# 1/7/20 11:00 PM scramble

# 11:06 - Prep finished

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
    
