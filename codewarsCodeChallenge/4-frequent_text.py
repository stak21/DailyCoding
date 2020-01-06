# 12/5/20 10:57 PM

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
#           if it is a word, append it to a dictionary with count of initial 1, or if it exists + 1
#           else move on
#           After that get the values and keys and sort them by the values
#           return the first three