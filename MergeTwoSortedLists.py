# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val        # Node value
        self.next = next      # Pointer to the next node

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]  # Head of the first sorted linked list
        :type list2: Optional[ListNode]  # Head of the second sorted linked list
        :rtype: Optional[ListNode]       # Head of the merged sorted linked list
        """
        # Create a dummy node as the starting point of the merged list
        dummy = ListNode(-1)
        
        # Use a pointer 'current' to build the merged list
        current = dummy
        
        # Iterate through both lists until one is exhausted
        while list1 and list2:
            if list1.val <= list2.val:  # Compare values of current nodes
                current.next = list1   # Append the smaller node to the merged list
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2   # Append the smaller node from list2
                list2 = list2.next     # Move to the next node in list2
            
            current = current.next     # Move the pointer forward in the merged list
        
        # Append the remaining nodes, if any, from either list
        current.next = list1 if list1 else list2
        
        # Return the merged list starting from the first node (skip dummy)
        return dummy.next

# Helper function to build a linked list from a list
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

sol = Solution()
list1 = build_list([1, 2, 4])
list2 = build_list([1, 3, 4])

merged_list = sol.mergeTwoLists(list1, list2)
print_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4]

print_list(sol.mergeTwoLists(build_list([]), build_list([])))      # Output: []
print_list(sol.mergeTwoLists(build_list([]), build_list([0])))     # Output: [0]
print_list(sol.mergeTwoLists(build_list([1]), build_list([2])))    # Output: [1, 2]

# Time Complexity: O(n + m)
#     n and m are the lengths of the two linked lists.
#     Each node is processed exactly once.

# Space Complexity: O(1)
#     No additional data structures are used—only pointers are manipulated.
