class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count={}#val,count

        for i in range(n):
            count[nums[i]]=1+count.get(nums[i],0)

        max_count=0
        max_val=0
        for val, curr_count in count.items():
            if curr_count >=max_count:
                max_val=val
                max_count=curr_count


        return max_val 
        