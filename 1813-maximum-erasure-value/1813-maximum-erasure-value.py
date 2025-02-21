class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        i=0
        curr_sum=0
        max_sum=0
        for j in range(len(nums)):
            while nums[j] in s:
                s.remove(nums[i])
                curr_sum-=nums[i]
                i+=1
            s.add(nums[j])
            curr_sum+=nums[j]
            max_sum=max(max_sum , curr_sum)
        return max_sum
            
        