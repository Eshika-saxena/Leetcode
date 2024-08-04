class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dict_nums={}
        dict_target={}
        for i in arr:
            if i in dict_nums:
                dict_nums[i]+=1
            else:
                dict_nums[i]=1
        for i in target:
            if i in dict_target:
                dict_target[i]+=1
            else:
                dict_target[i]=1
        if dict_nums.keys()!=dict_target.keys():
            return False
        for key in dict_nums:
            if dict_nums[key]!=dict_target[key]:
                return False
        return True
