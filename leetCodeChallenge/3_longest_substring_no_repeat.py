# Requrements:
#   Return the length of the longest substring with no repeats
#   empty string should return 0
#   iterate through every character
# Input:
#   "abc"
# Process:
#   Use a dictionary to store the index of characters and to find repeated characters
#   iterate through s as c
#   if c is in the dict
#       get the max count by finding the difference between the current index and the start
#       set the new starting point if it is further then the old one
# Notes:
#   becareful of where to put the start position (either + 1 or the same)
# Output:
#   3

def find_longest_substring(s: str) -> int:
    unique = {}
    max_count = start = 0

    if not s:
        return 0

    for index, c in enumerate(s):
        if c not in unique:
            max_count = max(max_count, index - start)
            start = max(start, unique[c] + 1)
        unique[c] = index

    return max(max_count, index - start + 1)

