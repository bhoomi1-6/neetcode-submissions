import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        n = len(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                continue
            else:
                return False
        return True 
            





        