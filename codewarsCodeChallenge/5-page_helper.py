# Requirements: 
#   Create a utility class for pagination to access information about the pages.
#   The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
#   The types of values contained within the collection/array are not relevant.
# I/O:
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# print(answer[0] == helper.page_count # should == 2
# print(answer[0] == helper.item_count # should == 6
# print(answer[0] == helper.page_item_count(0)  # should == 4
# print(answer[0] == helper.page_item_count(1) # last page - should == 2
# print(answer[0] == helper.page_item_count(2) # should == -1 since the page is invalid
print(answer[0] == 
# # page_ndex takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# print(answer[0] == helper.page_index(2) # should == 0
# print(answer[0] == helper.page_index(20) # should == -1
# print(answer[0] == helper.page_index(-10) # should == -1 because negative indexes are invalid
print(answer[0] == 
# Process:
# create a class that has 
#   attributes: 
#       page_count,:
#           set to length of the array / the items per page
#       item_count:
#           set to length of array
#       _page_cap:
#           set to iterms per page
#   instance:
#       page_item_count(page)
#           returns the number of items on the given page
#           if  page  < 0 or page > page_count, return -1
#           if page == page_count, return length of item_count % _page_cap
#           else  every page is filled, so return _page_cap
#       page_index(index)
#           returns the page of the given index
#           if 0 > index > item_count, return -1
#           return index // page_cap
#           page max    |   index       | page
#   ----------------------------------------
#               4           |       2           |      0
#               4           |       5           |       1
#           2 / 4 == 0
#           5 / 4 == 1
#           8 / 4 == 2

class PaginationHelper:
    def __init__(self, arr, page_cap):
        item_count = len(arr)
        self.item_count = item_count
        self.page_count = item_count // page_cap
        self._page_cap = page_cap
    
    def page_item_count(self, page):
        if page < 0 or  page > self.page_count:
            return -1
        if page == page_count:
            return self.item_count % self._page_cap
        return self._page_cap
    
    def page_index(self, index):
        if index < 0 or index > self.item_count:
            return -1
        return index // self._page_cap

tests = [
    (['a','b','c','d','e','f'], 4),
    (['a','b','c','d','e','f'], 1),
    (['a','b','c','d','e','f'], 8),
    (['a','b','c','d','e','f', 'g', 'h'], 4),
    (['a','b','c','d','e','f', 'g', 'h', 'i'], 4),
    ([], 4),
]

answers = [
    [2, 6, 4, 2, -1, 1, 0, -1, -1],
    [6, 6, 1, 1, -1, 5, 0, -1, -1],
    [1, 6, 8, 6, -1, 0, 0, -1, -1],
    [2, 8, 4, 4, -1, 1, 0, -1, -1],
    [3, 9, 4, 1, -1, 1, 0, -1, -1],
    [1, 0, 4, 0, -1, -1, -1, -1, -1],
]

for test, answer in zip(tests, answers):
    helper = PaginationHelper(test[0], test[1])
    print(answer[0] == helper.page_count) # should == 2
    print(answer[1] == helper.item_count) # should == 6
    print(answer[2] == helper.page_item_count(0))  # should == 4
    print(answer[3] == helper.page_item_count(1)) # last page - should == 2
    print(answer[4] == helper.page_item_count(4)) # should == -1 since the page is invalid
    print(answer[5] == helper.page_index(5)) # should == 1 (zero based index)
    print(answer[6] == helper.page_index(2)) # should == 0
    print(answer[7] == helper.page_index(20)) # should == -1
    print(answer[8] == helper.page_index(-10)) # should == -1 because negative indexes are invalid