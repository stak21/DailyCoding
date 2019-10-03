def maxProfit(prices):
    # I don't need to keep track of the bigger numbers if I find a smaller number
    # if the smaller number exists, then that profit will be bigger
    # iterate through 
    # keep track of the buy
    # if cur smaller than the buy, buy = cur
    # check next and find a profit
    # if profit is greater than max_proft, max_profit = profit
    if len(prices) is 0:
        return 0
    max_profit = 0
    buy = prices[0]
    for price in prices[1:]:
        if price < buy:
            buy = price
        else:
            profit = price - buy
            if profit > max_profit:
                max_profit = profit
    return max_profit
        
    
stocks = [[7,1,5,3,6,4], [7,6,4,3,1]]
for stock in stocks:
    print(maxProfit(stock))

'''
* Notes: initially I thought nested loops but that is way too slow, but it
should work
* I thought of various ways to do it, hash maps, two runs and dp. hash maps are
a no because there isn't any structure I could utilise. like I have the index,
but what can i use for that? two pass, I though maybe I could find the lowest
number and find the biggest number, but the problem was that the number could be
in the beginning which isn't the smallest number
* finally I knew it could be dp, but I wasn't sure how. I thought different
approaches, and I thought about three windows approach and it hit me that the
buy stock doesn't need to keep track of every number only the smallest along the
way and find the profit until the next smallest number.

'''
