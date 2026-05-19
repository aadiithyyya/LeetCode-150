class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_str = ""

        for i in s:
            if i.isalnum():
                filtered_str = filtered_str+i.lower()

        if filtered_str == filtered_str[::-1]:
            return True

        return False
        