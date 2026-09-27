class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        n=len(nums)
        i=0
        ans=[]
        while i<(2*n):
            for num in nums:
                ans.append(num)
                i+=1

        return ans

        