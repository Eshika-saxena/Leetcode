class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        list=[]
        cnt=0
        max_cnt=0
        for num in nums:
            if num==1:
                list.append(1)
                cnt+=1
                max_cnt=max(max_cnt , cnt)
            else:
                cnt=0
                list.clear()
        return max_cnt

        
        