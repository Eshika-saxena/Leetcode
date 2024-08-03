class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        mapp={}
        for i in nums:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
        for key , value in mapp.items():
            if value>(n//3):
                result.append(key)
        return result

        