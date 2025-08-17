class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1 and nums2 from the end
        p1, p2 = m - 1, n - 1
        # Start filling nums1 from the last index
        p = m + n - 1
        
        # Compare elements from the back and place the largest one at the current position
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Explanation:
# Key Observations:
#     Since both arrays are sorted:
#         We can use a two-pointer approach starting from the back to avoid overwriting elements in nums1.
#     Fill nums1 from the end to maintain in-place behavior.

# Approach:
#     Pointers Initialization:
#         p1: Points to the last element of the initialized part of nums1 (index m-1).
#         p2: Points to the last element of nums2 (index n-1).
#         p: Points to the last position in nums1 (index m+n-1).

#     Compare and Place:
#         Compare nums1[p1] and nums2[p2].
#         Place the larger element at nums1[p].
#         Move the corresponding pointer (p1 or p2) and decrement p.

#     Handle Remaining Elements:
#         If there are leftover elements in nums2, copy them to nums1.
#         No need to handle nums1 leftovers because they are already in place.

# Time Complexity: O(m + n)
#     Each element is processed once.

# Space Complexity: O(1)
#     In-place merging requires no extra space.

sol = Solution()

# Test case 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

# Test case 2
nums1 = [1]
m = 1
nums2 = []
n = 0
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

# Test case 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]
