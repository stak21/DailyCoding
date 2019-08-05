""" Square an array and sort it """
def sortedSquares(A):
    return sorted([item**2 for item in A])

li = [1, -2, 0, 20]
print (sortedSquares(li))

