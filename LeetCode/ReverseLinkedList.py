# Iterative Solution

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize previous pointer as None
        prev = None
        # Current pointer starts at the head
        current = head
        
        # Iterate through the linked list
        while current:
            # Temporarily store the next node
            next_node = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move the previous pointer to the current node
            prev = current
            # Move to the next node in the original list
            current = next_node
        
        # Return the new head of the reversed list
        return prev

# Recursive Solution

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: If head is None or only one node, return head
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list recursively
        reversed_head = self.reverseList(head.next)
        # Adjust the pointers
        head.next.next = head
        head.next = None
        
        # Return the new head of the reversed list
        return reversed_head

# Iterative Solution

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize previous pointer as None
        prev = None
        # Current pointer starts at the head
        current = head
        
        # Iterate through the linked list
        while current:
            # Temporarily store the next node
            next_node = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move the previous pointer to the current node
            prev = current
            # Move to the next node in the original list
            current = next_node
        
        # Return the new head of the reversed list
        return prev

# Recursive Solution

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: If head is None or only one node, return head
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list recursively
        reversed_head = self.reverseList(head.next)
        # Adjust the pointers
        head.next.next = head
        head.next = None
        
        # Return the new head of the reversed list
        return reversed_head

# Explanation:
# Iterative Approach:
#     Use two pointers:
#         prev to track the previous node (initially None).
#         current to iterate through the list (initially head).
#     For each node:
#         Temporarily store the next node (next_node).
#         Reverse the current node's pointer (current.next = prev).
#         Move the prev pointer to the current node.
#         Move the current pointer to the next node.
#     Once current becomes None, prev points to the new head of the reversed list.

# Recursive Approach:
#     Base Case:
#         If the list is empty or has one node, return the head.
#     Recursive Step:
#         Reverse the rest of the list (head.next).
#         Adjust the pointers for the current node: make head.next.next point to head and set head.next = None.
#     Return the new head of the reversed list.

# Complexity Analysis:
#     Time Complexity: O(n)
#         Both approaches process each node exactly once.

#     Space Complexity:
#         Iterative: O(1) (no additional space used).
#         Recursive: O(n) (due to the recursive call stack).

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

sol = Solution()

# Test case 1: [1,2,3,4,5]
head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = sol.reverseList(head)
print(linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]

# Test case 2: [1,2]
head = create_linked_list([1, 2])
reversed_head = sol.reverseList(head)
print(linked_list_to_list(reversed_head))  # Output: [2, 1]

# Test case 3: []
head = create_linked_list([])
reversed_head = sol.reverseList(head)
print(linked_list_to_list(reversed_head))  # Output: []
