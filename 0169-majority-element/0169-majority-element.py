class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        max_freq=0
        max_element=None
        for key ,value in hashmap.items():
            if value>max_freq:
                max_freq=value
                max_element=key
        return max_element


        