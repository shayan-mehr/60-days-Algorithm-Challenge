"""
Problem 007: Contains Duplicate II

Difficulty:
Easy

Description:
Given an integer array 'nums' and an integer 'k', return true if there are two distinct indices
i and j in the array such that:
    - nums[i] == nums[j]
    - abs(i - j) <= k

Otherwise, return false.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] == nums[3] and abs(0-3) = 3 <= 3

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Explanation: nums[2] == nums[3] and abs(2-3) = 1 <= 1

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Explanation: No two equal numbers within distance 2

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

Follow-up challenges:
1. Brute force — check all pairs (O(n²) time, O(1) space)
2. Hash Map storing last index (O(n) time, O(n) space)
3. Sliding window + Hash Set (O(n) time, O(k) space) - OPTIMAL for large k

Time complexity (optimal): O(n)
Space complexity (optimal): O(min(n, k))

Key insight (Hash Map approach):
    We only need to remember the most recent index of each number.
    Why? Because if a valid pair exists, the closest occurrence will
    satisfy the distance condition first. Any earlier occurrence is
    farther away, so it won't give us a better answer.

Algorithm (Hash Map with last index):
    1. Create an empty dictionary (num -> last_index)
    2. Iterate through array with index i:
        - If nums[i] exists in dictionary AND (i - last_index) <= k:
            return True
        - Update dictionary with current index (always keep the latest)
    3. Return False if loop completes

Alternative (Sliding Window + Set):
    1. Create an empty set (stores numbers in current window)
    2. Iterate through array with index i:
        - If nums[i] already in set: return True
        - Add nums[i] to set
        - If set size > k: remove nums[i-k] (slide window)
    3. Return False

Edge cases to consider:
    - k = 0: No pair possible because indices must be distinct
    - k >= array length: effectively checking entire array
    - All unique numbers: always returns false
    - Large k but array has duplicates far apart: works fine

Common mistakes:
    Forgetting that abs(i - j) <= k means both directions
    Storing first occurrence instead of last occurrence
    Not handling k = 0 properly
    Using O(n) space when k is small (sliding window better)

Comparison of approaches:

| Approach | Time | Space | Best when... |
|----------|------|-------|--------------|
| Brute Force | O(n²) | O(1) | Never (too slow) |
| HashMap (last index) | O(n) | O(n) | k is large |
| Sliding Window + Set | O(n) | O(k) | k is small |

Interview context:
    This is a follow-up to "Contains Duplicate I" (which only checks for
    any duplicate anywhere). The twist is adding the distance constraint.
    Interviewers love this progression:
        Q1: Contains Duplicate (easy)
        Q2: Contains Duplicate II (this problem)
        Q3: Contains Duplicate III (hard — uses bucket sort or balanced BST)

Real-world application:
    This pattern appears in:
    - Caching systems (check if recently used item is being reused)
    - Detecting near-duplicate messages in chat applications
    - Fraud detection (similar transactions within time window)

Common variations:
    - Contains Duplicate I (no distance constraint)
    - Contains Duplicate III (value difference constraint + index distance)
    - Find all pairs within distance k
"""


# nums = [7, 6, 8, 8, 1, 3, 10]
# i =     0  1  2  3  4  5  6
# k = 2

def contains_nearby_duplicate_brute_force(nums: list[int], k: int) -> bool:
    for i in range(len(nums) - 1): # i in range(6) -> 0, 1, 2, 3, 4, 5
        finial_index = min(i + k + 1, len(nums))  # min(2 + 1, 7) = 3
        for j in range(i + 1, finial_index): # range(1, 3)
            if nums[i] == nums[j]:
                return True
    return False

# test
from random import randint

def log_brute_force(n: int) -> bool:
    for i in range(n):
        l = randint(0, 10)
        nums = [randint(0, 10) for _ in range(l)]
        k = randint(0, len(nums))
        print(f"nums={nums}, k={k}  ->   {contains_nearby_duplicate_brute_force(nums, k)}")

# log_brute_force(10)


def contain_nearby_duplicate_hashmap(nums: list[int], k: int)-> bool:
    hashmap = {}
    for i in range(len(nums)):

        if nums[i] in hashmap:
            j = hashmap[nums[i]]
            if i - j <= k:
                return True
        hashmap[nums[i]] = i
    return False


def contain_nearby_duplicate_hashset(nums: list[int], k: int)-> bool:
    hash_set = set()
    for i in range(len(nums)):
        if nums[i] in hash_set:
            return True
        hash_set.add(nums[i])
        if len(hash_set) > k:
            hash_set.remove(nums[i-k])
    return False



def test(n: int) -> bool:
    for i in range(n):
        l = randint(0, 10)
        nums = [randint(0, 10) for _ in range(l)]
        k = randint(0, len(nums))
        brute_force = contains_nearby_duplicate_brute_force(nums, k)
        hash_map = contain_nearby_duplicate_hashmap(nums, k)
        hash_set = contain_nearby_duplicate_hashset(nums, k)
        errors = 0
        corrects = 100
        if brute_force != hash_set or hash_set != hash_map:
            errors += 1
            corrects -= 1
            print(f'nums: {nums}, k: {k}')
            print(f'brute force: {brute_force}')
            print(f'hash map: {hash_map}')
            print(f'{brute_force == hash_map == hash_set}')
            print('---------------------------------------')
    print(f'corrects: {corrects}')
    print(f'errors: {errors}')

# test(100)

print(contain_nearby_duplicate_hashset([1, 2, 3, 1], 3)) # True
print(contain_nearby_duplicate_hashset([1, 2, 3, 1], 2)) # False




