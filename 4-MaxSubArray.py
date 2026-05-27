
"""
Problem 004: Maximum Subarray

Difficulty:
Medium

Description:
Given an integer array 'nums', find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Follow-up challenges:
1. Brute force — check all subarrays (O(n^2) or O(n^3))
2. Divide and Conquer (O(n log n))
3. Kadane's Algorithm — single pass (O(n) time, O(1) space) - OPTIMAL

Time complexity (optimal): O(n)
Space complexity (optimal): O(1)

Key insight (Kadane's Algorithm):
At each position, decide whether to:
- Extend the existing subarray (add current element to running sum)
- Start a new subarray from the current element

If the running sum becomes negative, reset it to 0 because a negative sum
will only reduce any future subarray sum. Track the maximum sum seen so far.

History:
This problem has an interesting history. In the late 1970s, Ulf Grenander
posed the problem in 2D for image analysis. Michael Shamos proposed an
O(n log n) divide-and-conquer solution, and then Jay Kadane (a statistician)
solved it in O(n) after hearing about the problem — now known as Kadane's
Algorithm. [citation:2][citation:3]

Interview context:
Frequently asked at Amazon, Google, Microsoft, Apple, and Facebook.
"""

