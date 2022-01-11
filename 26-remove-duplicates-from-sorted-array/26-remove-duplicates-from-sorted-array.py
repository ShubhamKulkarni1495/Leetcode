class Solution(object):
    def removeDuplicates(self, nums):
        ind = 0
        while ind <len(nums)-1:
            if nums[ind] == nums[ind+1]:
                nums.remove(nums[ind])
                continue
            ind +=1

        return len(nums)