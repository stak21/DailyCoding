# Requirements: Return if the two arrays are "same"
#       the second array should have all the squared numbers on the right
#   I/O: [2,4], [4, 16] => True
#   Process
#       One approach would be to sort each one and iterate through checking if they are a pair.
#           if not return False

# approach one
def same(a1, a2):
    if len(a1) != len(a2):
        return False
    unique = set(a2)
    for e in a1:
        if e ** 2 not in unique:
            return False
    return True
