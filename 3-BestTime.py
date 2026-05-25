"""
Problem 003: Best Time to Buy and Sell Stock

Difficulty:
Easy-Medium

Description:
You are given an array 'prices' where prices[i] is the price of a given stock on day i.
You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell it.
Return the maximum profit. If no profit is possible, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price 1), sell on day 5 (price 6), profit = 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction possible

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Follow-up challenges:
1. Brute force with two loops (O(n²))
2. Single pass tracking minimum price so far (O(n) time, O(1) space) - OPTIMAL

Time complexity (optimal): O(n)
Space complexity (optimal): O(1)

Key insight:
Keep track of the minimum price seen so far.
At each day, calculate profit = current price - min_price.
Update max_profit if this profit is higher.

Interview context:
Commonly asked at Amazon, Google, Microsoft, Bloomberg.
"""

def test_and_log(func, args: list):
    for arg in args:
        print(f"input : {arg} | output : {func(arg)}")


def max_profit_brute_forec(prices: list):
    mx = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > mx:
                mx = profit
    return mx

# test max_profit_brute_force
test_and_log(max_profit_brute_forec, [[7,6,4,3,1], [7,1,5,3,6,4]])
# input : [7, 6, 4, 3, 1] | output : 0
# input : [7, 1, 5, 3, 6, 4] | output : 5
