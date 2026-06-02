class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i, val in enumerate(nums):

            diff = target - val

            if diff in h:
                return [h[diff], i]

            h[val] = i

                    
        