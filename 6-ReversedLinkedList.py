"""
Problem 006: Reverse Linked List

Difficulty:
Easy

Description:
Given the 'head' of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- Number of nodes in range [0, 5000]
- -5000 <= Node.val <= 5000

Node Definition:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Follow-up challenges:
1. Create new list using array (O(n) time, O(n) space)
2. Iterative reversal with three pointers (O(n) time, O(1) space) - OPTIMAL
3. Recursive reversal (O(n) time, O(n) stack space)

Time complexity (iterative optimal): O(n)
Space complexity (iterative optimal): O(1)

Key insight (Iterative approach):

Visual representation:
    Before:  null    1  ->  2  ->  3  ->  4  ->  5  ->  null
             prev   curr  next

    Step 1: Save curr.next (so we don't lose the rest of the list)
    Step 2: Point curr.next to prev (reverse the pointer)
    Step 3: Move prev to curr
    Step 4: Move curr to next_temp

    After iteration 1:  null <- 1    2  ->  3  ->  4  ->  5  ->  null
                     prev   curr

    After iteration 2:  null <- 1 <- 2    3  ->  4  ->  5  ->  null
                               prev   curr

    Final:  null <- 1 <- 2 <- 3 <- 4 <- 5
                                         prev (new head)

Three pointers needed:
    prev    - points to the previous node (starts as None)
    curr    - points to the current node (starts as head)
    next    - temporary pointer to save curr.next before overwriting

Algorithm (iterative):
    1. Initialize prev = None, curr = head
    2. While curr is not None:
        - Save next_temp = curr.next
        - Reverse pointer: curr.next = prev
        - Move prev forward: prev = curr
        - Move curr forward: curr = next_temp
    3. Return prev (new head)

Edge cases to consider:
    - Empty list (head = None) -> return None
    - Single node (head.next = None) -> return head (no change needed)
    - Two nodes (works naturally with algorithm)

Common mistakes:
    Losing reference to rest of list by not saving curr.next first
    Returning curr instead of prev at the end
    Off-by-one errors in loop condition

Visualization trick:
    Draw arrows between nodes on paper. The algorithm just reverses
    the direction of every arrow. Each iteration flips one arrow.

Interview context:
    This is THE warm-up problem for linked lists. Interviewers often
    start with this to see if you understand pointer manipulation.
    Many harder problems (Palindrome Linked List, Reverse Linked List II,
    Reverse Nodes in k-Group) build directly on this solution.

Variations to explore after solving:
    - Reverse Linked List II (reverse a portion of the list)
    - Reverse Nodes in k-Group (hard)
    - Palindrome Linked List (uses fast/slow + reverse)
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None




class LinkedList:
    def __init__(self):
        self.head = None



    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")


    def insert_at_beggining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


ll = LinkedList()
ll.insert_at_beggining(1)
ll.insert_at_beggining(2)
ll.insert_at_beggining(3)
ll.insert_at_beggining(4)
ll.display()


def reverseList(linked_list: LinkedList) -> LinkedList:
    current = linked_list.head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev



# how it works?
# prev = None
# current = Node(4, Node(3, Node(2, Node(1, None))))
# ------------------------------------------------------
# while 1:
# next_node = current.next = Node(3, Node(2, Node(1, None)))
# current.next = prev = None -> current = Node(4, None)
# prev = current = Node(4, None)
# current = next_node = Node(3, Node(2, Node(1, None)))
# -------------------------------------------------
# while 2:
# next_node = current.next = Node(2, Node(1, None))
# current.next = Node(4, None) =  None -> current = Node(3, Node(4, None))
# prev = current = Node(3, Node(4, None))
# current = next_node = Node(2, Node(1, None))
# --------------------------------------
# while 3:
# next_node = current.next = Node(1, None)
# current.next = prev = Node(3, Node(4, None)) -> current = Node(2, Node(3, Node(4, None)))
# prev = current = Node(2, Node(3, Node(4, None)))
# current = next_node = Node(1, None)
# ------------------------------------------
# while 4:
# next_node = current.next = None
# current.next = prev = Node(2, Node(3, Node(4, None))) -> current = Node(1, Node(2, Node(3, Node(4, None))))
# prev = current = Node(1, Node(2, Node(3, Node(4, None))))
# current = next_node = None
# ------------------------------------------




print("-" * 50)
print("Before reverse")
ll.display()
print("After reverse")
reverseList(ll)
ll.display()
