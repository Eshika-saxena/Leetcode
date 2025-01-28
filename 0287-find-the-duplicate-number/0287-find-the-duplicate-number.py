class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map={}
        for i in nums:
            if i in num_map:
                num_map[i]+=1
            else:
                num_map[i]=1
        for key , values in num_map.items():
            if values >1 :
                return key
        
        
        

        