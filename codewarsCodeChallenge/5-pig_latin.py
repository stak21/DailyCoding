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

def pig_it(text):
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split(' ')])
    
tests = ['hello', 'i am a pig', 'this has a punc !', 'why . am i ! a pig !']
answers = ['ellohay', 'iay maay aay igpay', 'histay ashay aay uncpay !', 'hyway . maay iay ! aay igpay !']
for test, answer in zip(tests, answers):
    res = pig_it(test)
    print(res, 'Success: ', res == answer)
    if res != answer:
        print("Expected", answer)