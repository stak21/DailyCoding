def isHappy(n: int) -> bool:
        original = {n}
        while True:
            next_num = 0
            digit = str(n)
            for i in digit:
                next_num += int(i) * int(i)
            if next_num == 1:
                return True
            if next_num in original:
                return False
            n = next_num
            original.add(next_num)

num = [2, 19]
for i in num:
    print(isHappy(i))

''' Notes:
    I wasn't sure if I had to return False, so I let it loop forever
    When i figured out it did need to return false, I knew i Needed to keep
    track of the original number
    I didn't keep in mind that other numbers could enter a loop, so I used a set
    to keep those in check
    '''

