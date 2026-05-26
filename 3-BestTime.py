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

def log(func, args: list):
    for arg in args:
        print(f"{func.__name__}({args}) returns {func(arg)}")


def max_profit_brute_force(prices: list):
    mx = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > mx:
                mx = profit
    return mx

# test max_profit_brute_force
# log(max_profit_brute_force, [[4, 100, 1, 80], [7, 6, 4, 3, 1], [7, 1, 5, 3, 6, 4]])
# input : [7, 6, 4, 3, 1] | output : 0
# input : [7, 1, 5, 3, 6, 4] | output : 5


def max_profit_single_pass(prices: list) -> int:
    if not prices:
        return 0
    max_profit = 0
    min_price = prices[0]

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if max_profit < prices[i] - min_price:
            max_profit = prices[i] - min_price
    return max_profit

# [4, 100, 1, 80]
# log(
#     max_profit_single_pass,
#     [[2, 4, 1, 7], [5, 4, 3, 2, 1], [7, 1, 5, 3, 6, 4], [0, 100, 12], [1], []]
# )

# testing single pass minimum tracking
from random import randint as rand

def test(n: int):
    test_inputs = []
    for i in range(n):
        temp = []
        for j in range(rand(0, 10)):
            temp.append(rand(0, 10))
        test_inputs.append(temp)


    errors = 0
    for i in range(n):
        brute_force = max_profit_brute_force(test_inputs[i])
        single_pass = max_profit_single_pass(test_inputs[i])
        check = brute_force == single_pass
        if not check:
            print(f"input: {test_inputs[i]} | BruteForce: {brute_force} | SinglePass: {single_pass} | {check}")
            errors += 1
    print(f"errors: {errors}")
    if not errors:
        print("All tests passed")
    else:
        print("Something went wrong")


# special_cases = [[10, 9, 8, 7, 100]]
# log(max_profit_brute_force, special_cases)
# log(max_profit_single_pass, special_cases)
# print("-" * 10)
test(1000000)
