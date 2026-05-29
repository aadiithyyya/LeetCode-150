class Solution:
    def isValid(self, s: str) -> bool:

        #step 1: initialize params
        stack = []
        hash_set = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in hash_set:
                if stack and stack[-1] == hash_set[c]:
                    stack.pop()

                else: 
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        