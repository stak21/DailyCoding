# Requirements:
#   Strip the comments ( which are passed in ) and everything else after
#   Remove all trailing white spaces
# I/O:
#  ('hello, there everyone I am # your father', ['#']) => 'hello, there everyone I am'
#   ('hello, there # commented out \n to be there \n Is sto # ry time is gone', ['#']) => 'hello, there \n to be there \n is sto'
#
# Process:
#   Thoughts: A simple approach would be to iterate through the whole string
#           if a character is a comment string, then mark that index
#           continue on until newline or end of string
#           if a newline is hit, slice everything from there to the newline 
#           continue from the newline and repeat
