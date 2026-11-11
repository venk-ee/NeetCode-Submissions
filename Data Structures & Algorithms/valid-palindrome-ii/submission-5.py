class Solution:
    def validPalindrome(self, s: str) -> bool:

        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                left_shifted=s[l+1:r+1]
                right_shifted=s[l:r]

                return left_shifted==left_shifted[::-1]or right_shifted==right_shifted[::-1]

            l+=1
            r-=1

        return True
        