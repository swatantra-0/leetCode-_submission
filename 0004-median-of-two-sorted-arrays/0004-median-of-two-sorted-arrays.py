class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        : type nums1 : list[int]
        : type nums2: list [int]
        : rtype : float 
        """
        nums3 = nums1+ nums2
        nums3.sort()
        m =  len (nums3)
        if m % 2 == 0  :
            median = (nums3[m//2 - 1] + nums3[m//2]) / 2.0
        else: 
            median = float(nums3[m//2])
        return median

        