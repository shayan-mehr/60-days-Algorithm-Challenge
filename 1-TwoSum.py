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

# 1. Brute force with two nested loops (O(n²))
def brute_force_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j==i:
                continue
            else:
                if nums[i] + nums[j] == target:
                    return [i, j]
    return None


# test brute_force_two_sum
# print(brute_force_two_sum([2, 7, 11, 15], 9))
# print(brute_force_two_sum([2, 7, 11, 15], 13))
# print(brute_force_two_sum([2, 7, 11, 15], 20))
# print(brute_force_two_sum([2, 7, 11, 15], 17))


# 2. Optimized using HashMap (O(n))

def two_sum_hash(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [i, hashmap[diff]]
        hashmap[nums[i]] = i
    return None

# test two_sum_hash
# print(two_sum_hash([2, 15, 11, 7], 13))
# print(two_sum_hash([15, 1, 3, 8], 9))
# print(two_sum_hash([1, 4, 2, 3], 8))
# print(two_sum_hash([1, 4, 2, 3], 6))


# 3. (Optional) Two pointers if array was sorted
def two_pointers(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
    return None

print(two_pointers([1, 2, 3, 4], 6))
print(two_pointers([5, 7, 10, 15], 12))
print(two_pointers([5, 10, 15, 20], 16))
print(two_pointers([-1, 0, 2, 10], 2))
