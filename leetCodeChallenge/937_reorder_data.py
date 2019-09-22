def reorderLogFiles(logs):
    # iterate through
    # # for every l, add that string into the letArr
    # # for every d, add that string into the digArr
    # # The digArr is added in order, but the letArr needs to be lexicographically order
    # # Figure out how to order them that way
    # # Combine the two array and return
    
    # def orderLexically(s, letArr):
    # # one idea is to split them by spaces, go through the 2nd word and figure out where to place them
    # place the first identifier in a dictionary for later use and store the other 
    # ex cat [car, zen]
    # I think use d&c to figure out the location by comparing the letters to the one in the dictionary
    # use equality to determine if its greater
    # if gerater then place after
    # if equal than check the identifier
    
    digArr = []
    letArr = []
    
    for log in logs:
        tok = log.split(' ', 1)
        if tok[1][0].isalpha():
            letArr.append(log)
        else:
            digArr.append(log)
    letArr.sort(key= lambda s: s.split(" ", 1)[0])
    letArr.sort(key= lambda s: s.split(" ", 1)[1])
    
    letArr.extend(digArr)
    return letArr

a = ["g1 act car","a8 act zoo","a2 act car","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
res = reorderLogFiles(a)
print(res)

#Note The idea was fine, but the execution was off.
# Instead of trying to figure out a complex sorting method (unless the interviewer asks)
# use sort with key(lambda)
