class Solution:
    def isValid(self, s: str) -> bool:

        #step 1: initialize params
        stack = []
        hash_set = {")":"(", "}":"{", "]":"["}

        #step 2: each char in string we check and if top of stack closing paranth
        #equals the char, we pop the stack
        for c in s:
            if c in hash_set:
                if stack and stack[-1] == hash_set[c]:
                    stack.pop()

                else: 
                    return False
            #step 3: if the char is open paranth, we keep appending
            else:
                stack.append(c)
                
        #return true if stack is empty else false
        return True if not stack else False
        