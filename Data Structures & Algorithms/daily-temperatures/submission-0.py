class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #step 1: initialize res array with 0's 
        res = [0] * len(temperatures)
        #initialize stack with [temp, index] as a pair
        stack = []

        #step 2: get index, temperature from input array
        for curr_index, curr_temp in enumerate (temperatures):

            #step 3: check if current temp is greater than stack top
            while stack and curr_temp > stack [-1][0]:

                #pop the first elemenet which is smaller, get the pair - temp and index
                prev_temp, prev_index = stack.pop()

                #subtract current temp index with smaller element index and update res
                res[prev_index] = curr_index - prev_index

            stack.append([curr_temp, curr_index])

        return res


        