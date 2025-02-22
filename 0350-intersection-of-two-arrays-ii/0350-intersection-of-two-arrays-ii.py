class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1={}
        hashmap2={}
        result=[]
        for num in nums1:
            if num in hashmap1:
                hashmap1[num]+=1
            else:
                hashmap1[num]=1
        for num in nums2:
            if num in hashmap2:
                hashmap2[num]+=1
            else:
                hashmap2[num]=1
        for key in hashmap1:
            if key in hashmap2:
                min_count = min(hashmap1[key], hashmap2[key])  # Take min frequency
                result.extend([key] * min_count) 
        return result

        
        