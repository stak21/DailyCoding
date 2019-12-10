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
    start = end = 0
    return_string = []
    stripping = False
    for index, c in enumerate(string):
        if c in comments and stripping is False:
            return_string.append(string[start:end])
            continue
        if c == '\n':
            if stripping is False:
                return_string.append(string[start:end])
            start =  index
            stripping = False
        end = index

    if stripping is False:
        return_string.append(string[start:end])
    return ''.join(return_string)

tests = [
    '1hello there', 
     '2hello # there', 
     '3hello there   ', 
     '4hello there    #   ', 
     '5hello # hide \n show and then ! hide this \n but show this', 
     '6hello \n show',
      '7hello there \n #hide',
      '8     \n hello'
      ]
answers = [
    '1hello there', '2hello', '3hello there', '4hello there', 
    '5helllo\n show and then\n but show this',
     '6hello\n show', '7hello there\n',
     '8\n hello',
     ]

for test, answer in zip(tests, answers):
    res = strip_comments(test, ['#', '!'])
    print(res, 'Success: ', res == answer)