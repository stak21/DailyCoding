 def countAndSay(self, n: int) -> str:
        #similar to factorial
        #I need to figure out how to read the values
        #ex: starting off with one, how am i going to read one 1
        # N will just be the number of rounds
        # I can start off with a "1"
        # "1" I can iterate through the string
        # store the current number
        # continue to iterate until the number is different, or end of string
        # concatenate the number of the number and the number
        #2 - 11 -
        # count_num = 1 count = 1
        # if cur EQ count_num? count += 1
        # else
        #   ret_str += str(count_num) + count_num
        #   count_num = cur,
        # output-> '21'
        #3 - '21'
        # count_num = 2, count = 1
        # next
        # if cur EQ count_num? count += 1; next
        # else
        # ret_str += str(count_num) + count_num
        # ret_str -> '12'
        # next
        # count_num = 1, count = 1
        # next
        # end
        # ret_str += str(count_num) + count_num
        # return ret_str

        if n == 1:
            return '1'
        
        count_num = '1'
        for term in range(n-1):
            ret_str = ''
            track = ''
            count = 0
            for cur in count_num:
                if not track:
                    track = cur
                if track == cur:
                    count += 1
                else:
                    ret_str += str(count) + str(track)
                    track = cur
                    count = 1
            ret_str += str(count) + str(track)
            count_num = ret_str
        return ret_str
