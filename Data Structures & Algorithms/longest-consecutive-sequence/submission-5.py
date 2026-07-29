class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0

        for num in nums:
            curr=num
            streak=1

            while(curr+1) in nums:
                curr+=1
                streak+=1

            res=max(res,streak)


        return res