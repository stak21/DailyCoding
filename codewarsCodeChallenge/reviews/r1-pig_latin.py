# 1/6/20 11:37 PM
# Test attempt 11:45 PM

# Requirements:
#   translate a string into pig latin
# I/O:
#   hello => ellohay
#   bye yo! => yebay oyay!
# Process:
#    parse the string 
#   for each word create a new pig latin word
# combine the parsed words and return

def pigify(string):
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in string.split(' ')])

tests = ['hello', 'hello all', 'hello all !']
answers = ['ellohay', 'ellohay llaay', 'ellohay llaay !']
for test, answer in zip(tests, answers):
    res = pigify(test)
    print(res, 'Success:', res == answer)
    if res != answer:
        print('Expected: ', res)