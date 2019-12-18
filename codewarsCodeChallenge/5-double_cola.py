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

def who_is_next(names, r):
    if not names:
        return None
    if r <= 1:
        return  names[0]
    name = names.pop(0)
    names.extend([name] * 2)
    return who_is_next(names, r - 1)

tests = [
    (['shoji'], 1),
    (['shoji'], 2),
    (['shoji', 'john'], 2),
    (['shoji', 'john'], 3),
    (['shoji', 'john', 'sara'], 3),
    (['shoji', 'jogn', 'sara'], 4),
    (['shoji', 'john', 'sara'], 10),
    ]
answers = ['shoji', 'shoji', 'john', 'shoji', 'sara', 'shoji', 'shoji']

for test, answer in zip(tests, answers):
    res = who_is_next(test[0], test[1])
    print(res, 'Success: ', answer == res)