# Result - 12/2/19 11:13 pm
# Failed to understand the question
# It asked to return the secret string using the triplets that were taken from the string
# not return a triplet


# Requirements:
#   The secret string to return is the first sequence 
#   Need to iterate through the entire string because the last character could make the shortest secret string
# Input:
#   ex: 'hello' ['hll', 'hel'] would return 'hel' because hel occurs before hll
# Process:
#   thoughts -  I could add up the index of every character's index
#       ex - h = 0,  l = 2, l = 3 -> 6
#               h = 0, e =1 , l = 2 -> 5
#               return the least 
#       another idea would be to take the first character and create a list of all the ones with the first character
#       then the next until there is one
#       if there is none for that character then reuse the previous list instead of the empty list
#       if there is more than 1 in the list, use that list
#       if there is just 1 return that string
#   Approach one:
#   iterate through the string
#       for each character, iterate through the triplets
#           using the triplet_index, return a list of triplets that have the matching character in the triplet_index
#           if the list is empty, move on
#           if the list length is 1, return the triplet
#           else  make that the new list 


def secret_triplet(secret, triplets):
    # Return the secret string
    # approach one:
    triplet_index = 0
    final_list = triplets
    for c in secret:
        filtered_list = [triplet for triplet in triplets if triplet[triplet_index] == c]
        if len(filtered_list) == 1:
            return filtered_list[0]
        if len(filtered_list) > 1:
            final_list = filtered_list
            triplet_index += 1

    
tests = [
    ('hello', ['hel', 'ell']),
    ('hello', ['elo', 'ell']),
    ('hello', ['hlo', 'ell']),
    ('hello', ['hel', 'hll', 'hlo']),
    ('hello', ['ell', 'elo', 'llo'])
]
answers = ['hel', 'ell', 'hlo', 'hel', 'ell']
for test, answer in zip(tests, answers):
    res = secret_triplet(test[0], test[1])
    print(res, 'Success: ', res == answer)

