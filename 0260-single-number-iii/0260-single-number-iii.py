class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap={}
        result=[]
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for key, value in hashmap.items():
            if value==1:
                result.append(key)
        return result
        