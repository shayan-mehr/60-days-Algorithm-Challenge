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
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome("pOP"))

