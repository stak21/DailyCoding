    def isAnagram(self, s: str, t: str) -> bool:
        # Input:
        #   'abba', 'baab' => true
        # Process:
        #   thought - we can get the count and return False if the count is off
        #       we can then add up the ascii value of each chracters and compare
        #       'feg' -> 6 + 5 + 7 = 18
        #   Scratch that idea
        #       
        #   Sorting is the obvious route
        #   because it is only one word we are dealing with we can use a hash to get the count
        if len(s) != len(t):
            return False
        word_count = {}
        for c in s:
            if c in word_count:
                word_count[c] += 1
            else:
                word_count[c] = 1    
        for c in t:
            if c in word_count and word_count.get(c) > 0:
                word_count[c] -= 1
            else:
                return False
        return True