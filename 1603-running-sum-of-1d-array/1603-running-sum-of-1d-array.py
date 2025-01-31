class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        prefixsum = [0] * len(nums)
        prefixsum[0]=nums[0]
        for i in range(1 , len(nums)):
            prefixsum[i]=nums[i]+prefixsum[i-1]
        return prefixsum

        