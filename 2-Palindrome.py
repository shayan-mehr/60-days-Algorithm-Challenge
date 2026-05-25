"""
Problem 002: Valid Palindrome

Difficulty:
Easy

Description:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After removing non-alphanumeric characters and lowercasing, we get "amanaplanacanalpanama" which reads the same forward and backward.

Example 2:
Input: s = "race a car"
Output: false
Explanation: Alphanumeric characters become "raceacar" which is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: After removing non-alphanumeric characters, we get an empty string which is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- String may contain letters, digits, spaces, and punctuation.

Follow-up challenges:
1. Filter + reverse (O(n) time, O(n) space)
2. Two pointers (O(n) time, O(1) space) - OPTIMAL

Time complexity (optimal): O(n)
Space complexity (optimal): O(1)

Key concepts:
- Two pointers (left and right)
- isalnum to check alphanumeric characters
- lower for case-insensitive comparison

Interview context:
Commonly asked at Amazon, Microsoft, and Facebook interviews.
"""



# 1. Filter + reverse (O(n) time, O(n) space)
def filter_non_alphanum(s: str) -> str:
    non_alphanum = {',', ' ', ':'}
    s = ''.join(filter(lambda x: x not in non_alphanum, s))
    return s

def isPalindrome(s: str) -> bool:
    s = s.lower() # non sensetive for uppercase and lowercase
    s = filter_non_alphanum(s)
    return s == s[-1::-1]

# test
# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))
# print(isPalindrome(" "))
# print(isPalindrome("pOP"))



# 2. Two pointers (O(n) time, O(1) space) - OPTIMAL
#p o p
#0 1 2 -> i = 0, j = 2

def is_palindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        if not s[left].isalnum():
            left += 1
        if not s[right].isalnum():
            right -= 1
    return True

def test_ispalindrome2(strings: list) -> bool:
    for s in strings:
        print(f'input: {s} | output: {is_palindrome_two_pointers(s)}')

strs = ["A man, a plan, a canal: panama", "race a car", "0P", "a.", "ab,a", "a,,b"]
test_ispalindrome2(strs)

