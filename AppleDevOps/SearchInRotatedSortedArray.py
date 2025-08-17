# =============================================================
# 7) Search in Rotated Sorted Array
# Problem:
#   Find index of target in rotated sorted array.
# Example: [4,5,6,7,0,1,2], target=0 -> 4
# =============================================================
def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target: return mid
        if nums[lo] <= nums[mid]:             # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        else:                                 # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid+1
            else:
                hi = mid-1
    return -1
