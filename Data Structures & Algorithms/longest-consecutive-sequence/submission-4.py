class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longeest=0
        seet=set(nums)

        for n in seet:
            if n-1 not in seet:
                next_num=n+1
                longest=1
                while next_num in seet:
                    longest+=1
                    next_num+=1

                longeest=max(longest,longeest)

        return longeest



            





        
        