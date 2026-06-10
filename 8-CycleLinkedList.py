"""
Problem 008: Linked List Cycle

Difficulty:
Easy

Description:
Given 'head', the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists if some node in the list can be reached again by continuously following
the 'next' pointer. Return true if there is a cycle, otherwise return false.

Note: 'pos' is not given as input. You only receive the head.

Example 1:
Input: head = [3,2,0,-4], cycle at index 1 (2 connects back to node 1)
Output: true
Explanation: The tail connects to the second node (2), creating a cycle.

Example 2:
Input: head = [1,2], cycle at index 0 (2 connects back to node 1)
Output: true
Explanation: The tail connects to the first node, creating a cycle.

Example 3:
Input: head = [1]
Output: false
Explanation: No cycle (single node points to None)

Example 4:
Input: head = []
Output: false
Explanation: Empty list has no cycle

Constraints:
- Number of nodes in range [0, 10^4]
- -10^5 <= Node.val <= 10^5

Node Definition:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

Follow-up challenges:
1. Hash Set approach — store visited nodes (O(n) time, O(n) space)
2. Fast and Slow Pointers (Floyd's Cycle Detection) — (O(n) time, O(1) space) - OPTIMAL

Time complexity (optimal): O(n)
Space complexity (optimal): O(1)

Key insight (Floyd's Cycle Detection Algorithm):

The Tortoise and Hare analogy:
    - Tortoise (slow) moves 1 step at a time
    - Hare (fast) moves 2 steps at a time
    - If there's a cycle, they MUST meet inside the cycle
    - If no cycle, hare will reach None (end) first

Why does this work mathematically?

    Let's say:
        - Distance from head to cycle start = a
        - Distance from cycle start to meeting point = b
        - Cycle length = L

    When slow enters cycle, fast is somewhere in cycle.
    By the time slow travels b, fast travels 2b.
    Since fast moves 2x speed, the relative speed is 1 step per move.
    So gap decreases by 1 each step → they eventually meet.

    Formal proof:
        - Let distance from head to meeting point = D
        - Slow moves D steps
        - Fast moves 2D steps
        - Difference = D which must be a multiple of cycle length
        - Therefore D is divisible by cycle length → they meet

Visual representation:

    No cycle:
        head → 1 → 2 → 3 → 4 → None
        slow → → → → → None (reaches end)
        fast → → → → → → → None (reaches end faster)

    With cycle:
        head → 1 → 2 → 3 → 4
                    ↑       ↓
                    6 ← 5 ←

        slow: 1 → 2 → 3 → 4 → 5 → 6 → 3 → 4 → 5 → 6 → 3...
        fast: 1 → 3 → 5 → 3 → 5 → 3... (faster, but within cycle)
        They meet at node 3 or 5

Algorithm:
    1. If head is None or head.next is None: return False
    2. Initialize slow = head, fast = head
    3. While fast is not None and fast.next is not None:
        - slow = slow.next (move 1 step)
        - fast = fast.next.next (move 2 steps)
        - If slow == fast: return True (cycle detected)
    4. Return False (fast reached end, no cycle)

Edge cases to consider:
    - Empty list (head = None) → return False
    - Single node with no cycle (head.next = None) → return False
    - Single node with cycle pointing to itself (not possible with next pointer)
    - Two nodes forming a cycle (node1.next = node2, node2.next = node1)
    - Very large cycle (works fine, O(n) time)

Common mistakes:
    Not checking fast.next before fast.next.next (causes None error)
    Initializing slow and fast differently (both should start at head)
    Only checking fast (need to check fast and fast.next)
    Using while loop incorrectly (infinite loop if condition wrong)

Comparison of approaches:

| Approach | Time | Space | Advantages | Disadvantages |
|----------|------|-------|------------|---------------|
| Hash Set | O(n) | O(n) | Simple, intuitive | Extra memory |
| Floyd's | O(n) | O(1) | No extra memory | Slightly complex |

Interview context:
    This is THE classic cycle detection problem. Interviewers expect:
        1. First mention hash set solution
        2. Then optimize to Floyd's algorithm with O(1) space
        3. Explain why it works mathematically
        4. Handle edge cases correctly

Real-world applications:
    - Detecting infinite loops in linked data structures
    - Memory leak detection in reference-counting systems
    - Deadlock detection in concurrent systems
    - Network routing loop detection

Common variations of this problem:
    - Find the start of the cycle (LeetCode 142)
    - Find the length of the cycle
    - Remove the cycle (fix the linked list)
    - Happy Number detection (LeetCode 202) — uses same idea
    - Find the duplicate number (LeetCode 287) — uses same idea

Follow-up questions interviewers may ask:
    Q: What if the linked list is very long (millions of nodes)?
    A: Floyd's algorithm still O(n) time, O(1) space — perfect.

    Q: Can we detect cycle using only one pointer?
    A: No, you need two pointers moving at different speeds.

    Q: What if we used 3-step and 1-step pointers?
    A: Works but might take more steps. 2 and 1 is optimal.

    Q: How to find cycle length after detection?
    A: Keep slow at meeting point, move fast until it returns.
"""



def hasCycle(head):
    pass