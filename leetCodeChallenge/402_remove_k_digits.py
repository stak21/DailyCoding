def removeKdigits(self, num: str, k: int) -> str:
    # iterate through num
    # i keep track of the first number
    # i check the next number
    # if the first number is smaller than the next number
    # drop that number
    # 
    # figure out how to remove a character from a string
    if not num:
        return '0'
    prev = num[0]
    remove = []
    for index, n in enumerate(num[1:]):
        if n < prev:
            prev = n
            remove.insert(0,index)
        else:
            remove.insert(0,index + 1)
        if len(remove) == k:
                break
    for index in remove:     
        num = num[:index] + num[index + 1:]

    if int(num) == 0:
        return num
    index = 0
    print(num)
    while True:
        if int(num[index]) == 0:
            index += 1
        else:
            break
    return num[index:]


''' Failiure first attempt 
I had the right idea, but I didn't execute well. I should have thought of a
better way to do this. Instead of removing, I should have thought to create
'''
