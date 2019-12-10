# Requirements:
#   Strip the comments ( which are passed in ) and everything else after
#   Remove all trailing white spaces
# I/O:
#        I =>('hello, there everyone I am # your father', ['#']) 
#       O => 'hello, there everyone I am'
#        I => ('hello, there # commented out \n to be there \n Is sto # ry time is gone', ['#']) 
#       O => 'hello, there \n to be there \n is sto'
#
# Process:
#   Thoughts: A simple approach would be to iterate through the whole string
#           if a character is a comment string, then mark that index
#           continue on until newline or end of string
#           if a newline is hit, slice everything from there to the newline 
#           continue from the newline and repeat

def strip_comments(string, comments):
    start = 0
    return_string = []
    stripping = False
    for index, c in enumerate(string):
        if c in comments and stripping is False:
            return_string.append(string[start:index])
            stripping = True
            continue
        if c == '\n' and stripping is True:
            # splice
            start = index
            stripping = False

    if stripping is False:
        return_string.append(string[start:].strip(' '))
    return ' '.join(return_string)

test = 'string is # live'
print(strip_comments(test, ['#']))