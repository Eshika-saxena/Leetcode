class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap=[]
        for i in range(k):
            heappush(min_heap , int(nums[i]))
        for i in range(k,len(nums)):
            if min_heap[0]<int(nums[i]):
                heappop(min_heap)
                heappush(min_heap , int(nums[i]))
        return str(min_heap[0])

        