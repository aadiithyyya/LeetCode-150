from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if Counter(list(s))== Counter(list(t)) else False
        