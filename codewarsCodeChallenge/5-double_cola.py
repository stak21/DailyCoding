# Started: 12/17/19 10:56 PM

#   Requirements:
#   Given a list of names in a queue, each name that gets popped returns to the queue, but as two. Return the name of the nth person that gets popped
#   I/O:
#       ['shoji', 'john',], 4
#       index   |   new list
#---------------------------
#           0       |       ['john', 'shoji', 'shoji'] => 'shoji'
#           1       |       ['shoji', 'shoji', 'john', 'john'] => 'john'
#           2       |       ['shoji', 'john', 'john', 'shoji' ,'shoji'] =< 'shoji'
#           3       |       ['john', 'john', 'shoji', 'shoji', 'shoji' ,, 'shoji']a => 'shoji

#   Process: 
#   Ideas - recursion pass in the array with the number
#                   each pass through, it will pop the first item and add 2 to the end
#                   once it reaches 0, return the name at the end