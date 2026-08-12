class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count={}
        max_cnt=0
        res=0

        for i,n in enumerate(nums):
            count[n]=1+count.get(n,0)

        for num,cnt in count.items():
            if max_cnt<cnt:
                res=num
                max_cnt=cnt
        
        return res
        
