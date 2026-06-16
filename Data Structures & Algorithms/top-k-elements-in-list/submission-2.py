from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counted = Counter(nums)
        sorted_nums = sorted(nums_counted.items(),key= lambda x:x[-1], reverse = True)
        res= []
        for i in range (k):
            res.append(sorted_nums[i][0])
        return res
        