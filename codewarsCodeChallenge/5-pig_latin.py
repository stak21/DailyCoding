# 1/2/20 11:13 PM

# Requirements:
#   Given a string, turn it into pig latin except for any punctuation
#  I/O:
#   hello => ellohay
#   i am a pig => iay maay aay igpay
#   This has a punc! => histay ashay aay uncpay!
# Process:
#   parse each word
#   create a new string with the first letter last and add 'ay' 
#   if it is a punctuation don't do anything