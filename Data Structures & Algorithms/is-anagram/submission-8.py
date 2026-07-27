class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=len(s)
        T=len(t)

        if S!=T:return False

        return sorted(s) == sorted(t)
            
        