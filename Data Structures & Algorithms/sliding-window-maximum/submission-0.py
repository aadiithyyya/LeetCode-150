from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #step1: initialize params
        l,r = 0,0
        res = []
        dq = collections.deque()

        #step 2: loop till r reaches end of list

        while r< len(nums):

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            #step 3 see step 4 before step 3: 
            #check if appened queue element is smaller than existing left element 
            #and l is inbounds

            if l > dq[0]:
                dq.popleft()

            #step4: append leftmost val and update pointers to stay inbounds(for l) 

            if (r+1) >= k:
                res.append(nums[dq[0]])
                l+=1
            r+=1

        return res

