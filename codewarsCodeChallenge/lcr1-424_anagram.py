#Write a function that will find all the anagrams of a word from a list. 
#You will be given two inputs a word and an array with words. 
#You should return an array of all the anagrams or an empty array if there are none.
# Requirements:
#   should ignore words that do not have the same count
#   probably use sort and a cache
# Input:
#   'word', ['wrod', wdro', 'dog'] - ['wrod', 'wdro']
# Process:
#   iterate through each word in the list
#       sort the word and store the actual word in a dictionary with the sorted_word beiing the key
#    do the same with the word, but on the outside so we only sort once
#       return the dictionary with the key, or an empty array

def anagram(word, words):
    word_cache = {}
    word_len = len(word)
    for w in words:
        if len(w) != word_len:
            continue
        sorted_word = ''.join(sorted(w))
        if sorted_word in word_cache:
            word_cache[sorted_word].append(w)
        else:
            word_cache[sorted_word] = [w]
    sorted_word = ''.join(sorted(word))
    return word_cache.get(sorted_word, [])

tests = [('word', ['wrod', 'wdro', 'dog'])]
answers = [['wrod', 'wdro']]

for test, answer in zip(tests, answers):
    res = anagram(test[0], test[1])
    print(res, 'Success: ', res == answer)