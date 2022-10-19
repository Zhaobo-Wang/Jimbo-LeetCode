'''
###

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
###

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy
        right = 1 # sell
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]  # calculate the current profit
            if current_profit > 0:
                max_profit = max(current_profit, max_profit)  # compare the max profit with current profit, which one is bigger
            else:
                left = right # if current profit is negative, then go to next day to buy stock
            right += 1  # go through all day sell
        return max_profit
            