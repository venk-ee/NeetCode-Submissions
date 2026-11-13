class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        place=[]

        for i in range(len(nums)):
            if nums[i]in place:
                return True
            else:
                place.append(nums[i])

        return False

        