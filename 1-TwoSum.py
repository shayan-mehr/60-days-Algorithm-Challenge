"""
Problem 001: Two Sum

Difficulty:
Easy / Medium

Description:
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.
You may assume each input has exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid solution exists.

Follow-up challenges:
1. Brute force with two nested loops (O(n²))
2. Optimized using HashMap (O(n))
3. (Optional) Two pointers if array was sorted

Time complexity (optimal): O(n)
Space complexity (optimal): O(n)

Interview context:
Commonly asked at Amazon, Google, Microsoft, and Facebook.
"""
