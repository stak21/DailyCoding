# Requirements: 
#   Create a utility class for pagination to access information about the pages.
#   The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
#   The types of values contained within the collection/array are not relevant.
# I/O:
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count # should == 2
# helper.item_count # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_ndex takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

# Process:
