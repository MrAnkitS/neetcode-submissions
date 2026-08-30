class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for x in s:
            if x in t:
                t = t.replace(x,'',1)
            else:
                return False
        if t == '':
            return True 
        return False