class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts=[0,0,0]

        for colors in nums:
            counts[colors]+=1

        r,g,b=counts

        nums[:r]=[0]*r
        nums[r:r+g]=[1]*g
        nums[r+g:]=[2]*b

