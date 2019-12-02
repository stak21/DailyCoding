# Anagram
# Requirements:
#   Write a function that returns a list of all the possible anagrams
#   given a word and a list of words to create the anagram with  
# Input:
#   'abba', ['baab', 'abcd', 'baba', 'asaa'] => ['baab, 'baba']
# Process:
#   Thoughts  - I would need to create every permutation of the given word and check the list for each one
#           example: 'a' in ['a', 'ab', 'c'] -> true, but would 'a' in 'ab' be true too? The answer is no
#       Naive approach: a possible naive approach is to sort each word and put each one in a dictionary with a list of the matching letters.
#       Approach 1: change each character in different arrangements and check if that character is in the list

# Naive approach
def is_anagram(word, words):
    matchings = {}
    for w in words:
        sorted_word = ''.join(sorted(w))
        if sorted_word in matchings:
             matchings[sorted_word].append(w)
        else:
            matchings[sorted_word] = [w]
    sorted_word = ''.join(sorted(word))
    return matchings.get(sorted_word, [])

tests = [('a', ['a', 'b', 'ab']), ('aba', ['aab', 'baa', 'abb']), ('ab', ['a'])]
answers = [['a'], ['aab', 'baa'], []]
for test, answer in zip(tests, answers):
    res = is_anagram(test[0], test[1])
    print(res, 'Success: ', res == answer)