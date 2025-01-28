class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_map={}
        temp=[]
        n=len(nums)
        for i in nums:
            if i in num_map:
                num_map[i]+=1
            else:
                num_map[i]=1
        for i in range(1,n+1):
            if i not in num_map:
                temp.append(i)
        return temp

        