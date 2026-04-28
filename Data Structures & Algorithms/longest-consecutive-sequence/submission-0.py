class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0

        for n in numset:
            if (n-1) not in numset:
                current_length=1

                while (n+current_length) in numset:
                    current_length+=1
                longest=max(longest,current_length)
        return longest