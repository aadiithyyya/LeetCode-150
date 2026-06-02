class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strs_hash={}

        if len(t) != len(s):
            return False

        for s_element, t_element in zip(s,t):
            strs_hash[s_element] = strs_hash.get(s_element, 0) + 1
            strs_hash[t_element] = strs_hash.get(t_element, 0) - 1

        for check in strs_hash.values():
            if check != 0:
                return False
        return True


        
        