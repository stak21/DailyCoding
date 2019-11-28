# Requirements:
#   given two arrays, return true if the numbers in the second array have the first arrays square multiplicities
# Input:
#   [2, 4, 6] [4, 16, 36] -> True
#   [] [] -> True
#   [] None -> False
#   [2, 3] [3, 9] -> False
# Process:
#   check for any None values
#   if array1 is empty return True
#   
#   Approach 1:
#       iterate through array 1
#       if the sq of the number is in array2, remove it from array 2
#       else return False
#       if array 2 still has values, return False
#       else return True
#   Approach 2:
#       iterate through both arrays sorted
#       if the sq of array1's number is not equal to array2's number
#       return False

# Approach 1:
def same_1(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    for n in array1:
        sq = n ** 2
        if sq in array2:
            array2.remove(sq)
        else:
            return False
    return True

# Approach 2:
def same_2(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    for a1, a2 in zip(sorted(array1), sorted(array2)):
        if (a1 ** 2) != a2:
            return False

    return True
                
            
tests = [([2, 4], [4,16]), ([2, 4],[3,16]), ([], None), (None, []), ([], []), ([], [2])]
answers = [True, False, False, False, True, False]
for test, answer in zip(tests, answers):
    res = same_2(test[0], test[1])
    res2 = same_1(test[0], test[1])
    print(res, 'Success: ', res == answer)
    print(res2, 'Success: ', res2 == answer)



