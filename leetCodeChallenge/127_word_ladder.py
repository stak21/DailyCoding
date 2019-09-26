class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # given a beginword, endword and a wordlist find the least amount of transformation needed to get to the endword
        # only one letter can be transformaed at a time
        # hit - > cog  , [hot, hut, dog dot cog]
        # h_t o u
        # hi_
        # potential = [(1,hot) , (2,hir), (2,hiq)]
        # end word = cog
        # check r and q with cogs g none match
        # check o with o on cog, it matches
        # naive solution could possibly be find a word in the list that has 2 of the letters
        # create a list of all the possible words
        # iterate through the end word to see if any of its characters are in that list
        # if it is, transform the begin word to that word and repeat the same process
        def bfs(word_list, c):
            
            return (potential)
        count = 0
        while True:
            if beginWord == endWord:
                return count
            potential_words = dfs(word_list, beginWord)
            for index, word in potential_words:
                if word[index] == endWord[index]:
                    beginWord = word
                    count += 1
                    break
            return 0
