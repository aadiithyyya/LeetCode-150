class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numsSet:
                current_length = 0
                while (n+current_length) in numsSet:
                    current_length +=1
                longest = max(longest,current_length)    
        return(longest)   