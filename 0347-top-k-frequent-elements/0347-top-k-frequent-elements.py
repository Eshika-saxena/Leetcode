class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        max_heap=[]
        for num,freq in hash_map.items():
            heappush(max_heap,(-freq , num))
        result=[]
        for _ in range(k):
            result.append(heappop(max_heap)[1])
        return result
            
            

    

        