class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums2)):
            if nums1[i+m]==0:
                nums1[i+m]=nums2[i]
        return nums1.sort() 