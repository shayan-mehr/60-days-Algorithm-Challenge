"""
Problem 005: Valid Parentheses

Difficulty:
Easy

Description:
Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A valid string must satisfy:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

Follow-up challenges:
1. Replace method (inefficient, O(n²))
2. Stack with hash map (O(n) time, O(n) space) - OPTIMAL

Time complexity (optimal): O(n)
Space complexity (optimal): O(n)

Key insight (Stack approach):
- When you see an opening bracket, push it onto a stack.
- When you see a closing bracket, pop from the stack and check if it matches.
- At the end, the stack must be empty.

Matching pairs (hash map):
    closing -> opening
    ')': '('
    '}': '{'
    ']': '['

Edge cases to consider:
- Empty string? (constraints say length >= 1, but good to think about)
- String starts with closing bracket: stack is empty, return false immediately
- String ends with opening bracket: stack not empty at the end, return false
- Nested brackets like "({[]})": stack handles depth correctly

History:
This problem comes from compiler design and expression parsing. The concept of
matching parentheses dates back to early programming languages like ALGOL 60,
where balanced parentheses were critical for block structure.

Interview context:
One of the most frequently asked easy problems. Interviewers love this because
it tests understanding of:
- Stack data structure
- Hash maps for quick lookups
- Edge case handling
- Clean, readable code

Common variations:
- Remove outermost parentheses
- Minimum add to make parentheses valid
- Longest valid parentheses (harder)
"""


class Stack:
    def __init__(self):
        self.__stack = []
        self.__top = -1

    def is_empty(self):
        return self.__top == -1

    def top(self):
        return self.__top

    def push(self, value):
        self.__stack.append(value)
        self.__top += 1

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__stack[self.__top]

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack is not possible')
        temp = self.__stack.pop(self.__top)
        self.__top -= 1
        return temp


# test Stack
a = [1, 2, 3, 4]

astack = Stack()

for i in a:
    astack.push(i)

print(astack.pop()) # 4
print(astack.top()) # 2
print(astack.pop()) # 3
print(astack.top()) # 1
print(astack.is_empty()) # False
print(astack.pop()) # 2
print(astack.pop()) # 1
print(astack.is_empty()) # True
print(astack.top()) # -1
print(astack.pop()) # IndexError
