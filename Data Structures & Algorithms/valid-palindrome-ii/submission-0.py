class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                left_shift=s[l+1:r+1]
                right_shift=s[l:r]
                return (left_shift==left_shift[::-1]or right_shift==right_shift[::-1])

            l+=1
            r-=1
        return True
            
