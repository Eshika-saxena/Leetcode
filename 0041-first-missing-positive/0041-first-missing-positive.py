class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_map={}
        for num in nums:
            if num>0:
                num_map[num]=True
        for i in range(1, len(nums)+2):
            if i not in num_map:
                return i 

        
        