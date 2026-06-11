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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# implement Cycle just with "Node"
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
#
# a.next = b
# b.next = c
# c.next = d
# d.next = a
# print(a.next.next.next.next.data) # output = a.data = 1

# class CycleLinkedList:
#     def __init__(self):
#         self.head = None
#
#
#     def append(self, data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#             new_node.next = self.head
#
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
#     def append(self, data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#             new_node.next = None
#
#         else:
#             new_node = Node(data)
#             new_node.next = None
#
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node
#             new_node.next = None
#
#
#
# # Test CycleLinkedList
# # l = CycleLinkedList()
# # l.append(1)
# # l.append(2)
# # l.append(3)
# # l.append(4)
# # for i in range(10):
# #     print(i, ':', l.next())
#
#


# cll = CycleLinkedList()
# cll.append(1)
# cll.append(2)
# cll.append(3)
# cll.append(4)
#
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)





cll = []
ll = []
for i in range(4):
    cll.append(Node(i))
    ll.append(Node(i))

# Cycle Linked List
cll[0].next = cll[1]
cll[1].next = cll[2]
cll[2].next = cll[3]
cll[3].next = cll[0]

# test
# h = cll[0]
# for i in range(10):
#     print(h.data)
#     h = h.next

# Linked List
ll[0].next = ll[1]
ll[1].next = ll[2]
ll[2].next = ll[3]
ll[3].next = None


# Floyd's approch(fast and slow pointers)
def hasCycle(head):
    fast = head
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(hasCycle(ll[0]))      # output: False
print(hasCycle(cll[0]))     # output: True




# linked list (within cycle)
# slow : .  |  fast : -
#   1   2   3   4   None
#   .-
#       .   -
#           .       -        ====> return False, becaues Fast is None

# cycle linked list
# slow : .  |  fast : -
#   1   2   3   4
#   .-
#       .   -
#   _       .
#           _   .
#   ._               =====> return True, because slow == Fast
