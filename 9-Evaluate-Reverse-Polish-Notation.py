"""
Problem 009: Evaluate Reverse Polish Notation (RPN)

Difficulty:
Medium

Description:
You are given an array of strings 'tokens' that represents an arithmetic expression
in Reverse Polish Notation (RPN). Evaluate the expression and return the result as an integer.

Valid operators are: '+', '-', '*', '/'
Each operand may be an integer or another expression.
Division between two integers should truncate toward zero.
The given RPN expression is always valid (no division by zero).

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 4 + 2 = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation:
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator ("+", "-", "*", "/") or an integer in range [-200, 200]

Follow-up challenges:
1. Recursive evaluation (more complex, not needed)
2. Stack-based evaluation (O(n) time, O(n) space) - OPTIMAL
3. Evaluate RPN with variable support

Time complexity (optimal): O(n)
Space complexity (optimal): O(n)

Key insight (Stack approach):

What is Reverse Polish Notation (RPN)?
    - Also called postfix notation
    - Operators come AFTER their operands
    - No parentheses needed — order is unambiguous

Example: "3 4 +" means "3 + 4"
Example: "5 1 2 + 4 * + 3 -" = (5 + ((1 + 2) * 4)) - 3

Why stack works perfectly:
    - When you see a number: push it onto the stack
    - When you see an operator: pop two numbers, apply operator, push result
    - At the end, the last remaining number is the answer

Algorithm step by step:
    1. Initialize an empty stack
    2. For each token in tokens:
        a. If token is an operator:
            - right = stack.pop() (first pop is right operand)
            - left = stack.pop()  (second pop is left operand)
            - result = apply_operator(left, right, token)
            - stack.append(result)
        b. If token is a number:
            - stack.append(int(token))
    3. Return stack[0] (the final result)

Operator order is critical:
    For subtraction: left - right (not right - left)
    For division:   left / right (not right / left)

    Example: tokens = ["3","4","-"]
        pop right = 4
        pop left = 3
        result = 3 - 4 = -1 ✓ (not 4 - 3 = 1 ✗)

Truncate toward zero (important!):

| Language | -3 // 2 | int(-3/2) |
|----------|---------|-----------|
| Python   | -2      | -1        |
| Java     | -1      | -1        |
| C++      | -1      | -1        |

In Python, use int(left / right) instead of left // right
    - int(-3 / 2) = int(-1.5) = -1 ✓ (truncates toward zero)
    - -3 // 2 = -2 (floors toward negative infinity)

Visual representation for "2 1 + 3 *":

    Step 1: "2" → stack = [2]
    Step 2: "1" → stack = [2, 1]
    Step 3: "+" → pop 1, pop 2 → 2+1=3 → stack = [3]
    Step 4: "3" → stack = [3, 3]
    Step 5: "*" → pop 3, pop 3 → 3*3=9 → stack = [9]
    Return: 9

Edge cases to consider:
    - Single number: ["5"] → return 5
    - Negative numbers: "-11" → int("-11") = -11
    - Division with negative numbers: int(-13/5) = -2
    - Very large numbers: within constraints, but Python handles big ints
    - Division by zero: not possible (problem guarantees valid input)

Common mistakes:
    Using left // right instead of int(left / right) — fails for negatives
    Popping right before left incorrectly (right = pop first is correct)
    Not converting strings to int for numbers
    Forgetting to check if token is operator vs number
    Using float division (need integer division truncating toward zero)

Comparison with infix notation:

| Infix (normal) | RPN (postfix) |
|----------------|---------------|
| (2 + 1) * 3    | 2 1 + 3 *     |
| 2 + 1 * 3      | 2 1 3 * +     |
| (2 + 1 * 3)    | 2 1 3 * +     |

RPN advantages:
    - No parentheses needed
    - No operator precedence rules to handle
    - Easy to evaluate with a stack
    - Used in some calculators (HP calculators)

Interview context:
    This is THE classic stack application problem. Interviewers love it because:
        - Tests understanding of stacks
        - Tests handling of operator precedence implicitly
        - Tests edge cases with division and negative numbers
        - Can be extended to support more operators

Real-world applications:
    - Stack-based calculators (HP, RPN calculators)
    - Compilers (converting infix to postfix)
    - Interpreting mathematical expressions
    - Symbolic math systems
    - Forth programming language

Common variations:
    - Validate RPN expression (check if valid)
    - Infix to postfix conversion (Shunting-yard algorithm)
    - Evaluate expression with variables
    - Handle unary operators (negative sign)

Follow-up questions interviewers may ask:
    Q: How would you handle more operators like "^" (power) or "%" (modulo)?
    A: Add them to the operator set with appropriate behavior.

    Q: What if the expression has floating point numbers?
    A: Use float instead of int, but division behavior changes.

    Q: Can we evaluate RPN with O(1) space?
    A: No, we need stack O(n) because we need to store operands.
"""


def evalRPN(tokens: list[str]) -> int:
    # your code here
    pass