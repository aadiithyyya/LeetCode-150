class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = {}

        for w in strs:
            sorted_word = "".join(sorted(w))

            if sorted_word not in h:
                h[sorted_word]= []

            h[sorted_word].append(w)
        return list(h.values())

        