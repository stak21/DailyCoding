# 12/5/20 10:57 PM

# 11:18 PM Attemp1

# 11:40 PM Success on personal tests

# Requirements:
#   Given a string of text, return the top three most frequent words
#   matched words are case-insensitive
#   words that are tied are place arbitrarily
#   there can be apostrophes, but other punctuations can be ignored
#   a word is all alphabetical with apostraphes allowed
# I/O:
#   Hello there I => [hello, there, i]
#   hello, I am hello be I want am hello => [hello, i, am]
#   I can't hear you, but I can't hear => [can't, i, hear]
# Process:
#   Idea- Parse by spaces
#           verify each item as a word
#               How to veirfy? Easiest solution is to iterate through each letter and if it isn't alpha or an apostrephe next word
#           if it is a word, append it to a dictionary with count of initial 1, or if it exists + 1
#           else move on
#           After that get the values and keys and sort them by the values
#           return the first three

def top_3_words(text):

    def is_word(string):
        if not string:
            return False
        if len(string) == 1 and string == '\'':
            return False
        if '\'\'' in string:
            return False
        for c in string:
            if not c.isalpha() and c is not '\'':
                return False
        return True

    def word_tok(text):
        tok = []
        start = 0
        is_word = False
        for index, c in enumerate(text):
            if not is_word and c.isalpha() or not is_word and c is '\'':
                start = index
                is_word = True
            if is_word and not c.isalpha() and c is not '\'':
                tok.append(text[start:index])
                is_word = False
        tok.append(text[start:])
        return tok
    parsed = word_tok(text)
    cache = {}
    for word in parsed:
        word = word.lower()
        if is_word(word):
            print(word)
            if word in cache:
                cache[word] +=1
            else:
                cache[word ]= 1
    sorted_words = [word for word, count in sorted(cache.items(), key=lambda item: item[1], reverse=True)]
    return sorted_words[:3]

tests = ['Hello there I', 'hello hello, I am hello i be I want am hello', 'I can\'t hear you, but I can\'t hear can\'t']
answers = [['hello', 'there', 'i'], ['hello', 'i', 'am'], ['can\'t', 'i', 'hear'] ]

for test, answer in zip(tests, answers):
    res = top_3_words(test)
    print(res, 'Success: ', res == answer)
    if res != answer:
        print("Expected", answer)