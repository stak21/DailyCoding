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
    
