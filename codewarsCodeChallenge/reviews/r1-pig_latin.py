# 1/6/20 11:37 PM
# Test attempt 11:45 PM Success
# Test attempt 11:47PM 2 more tests
# Success with all tests: 11:58 PM

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
    pigified = []
    for word in string.split(' '):
        if len(word) == 1 and not word.isalpha():
            pigified.append(word)
        elif word[-1].isalpha():
            pigified.append(word[1:] + word[:1] + 'ay')
        else:
            pigified.append(word[1:-1] + word[:1] + 'ay' + word[-1])
        
    return ' '.join(pigified)

tests = ['hello', 'hello all', 'hello all !', 'hello ! all', 'hello all!']
answers = ['ellohay', 'ellohay llaay', 'ellohay llaay !', 'ellohay ! llaay', 'ellohay llaay!']
for test, answer in zip(tests, answers):
    res = pigify(test)
    print(res, 'Success:', res == answer)
    if res != answer:
        print('Expected: ', answer)