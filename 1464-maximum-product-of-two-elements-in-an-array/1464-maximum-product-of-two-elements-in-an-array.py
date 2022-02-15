class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = nums[0]
        b = nums[1]
        if a > b:
            a, b = b, a
        # maintain a < b
        for i in range(2, len(nums)):
            if nums[i] > b:
                a = b
                b = nums[i]
            elif nums[i] > a:
                a = nums[i]
        return (a - 1) * (b - 1)