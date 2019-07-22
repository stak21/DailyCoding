""" return the n repeated numbers in the given list """
def repeatedNTimes(self, A: List[int]) -> int:
        unique_sum = sum(A) - sum(set(A)) 
        return int(unique_sum / (len(A) / 2 - 1))
