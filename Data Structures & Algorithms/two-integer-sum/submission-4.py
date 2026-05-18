class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,val in enumerate(nums):
            h_v = target - val

            if h_v in h:
                return[h[h_v],i]

            h[val]=i


                    
        