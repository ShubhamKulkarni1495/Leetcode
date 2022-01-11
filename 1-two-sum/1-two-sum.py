class Solution:
    def twoSum(self, nums, target):
        dictionary={}
        l=len(nums)
        for i in range(l):
            if target-nums[i] not in dictionary.keys():
                dictionary[nums[i]]=i
            else:
                break
        l=[i,dictionary[target-nums[i]]]
        return l