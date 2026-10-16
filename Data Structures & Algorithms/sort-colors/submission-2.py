class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        flag=True
        while flag:
            flag=False
            for i in range(1,n):
                if nums[i-1]>nums[i]:
                    nums[i-1],nums[i]=nums[i],nums[i-1]
                    flag=True
        