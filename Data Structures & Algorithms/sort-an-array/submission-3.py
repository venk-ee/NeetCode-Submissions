class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.buble_sort(nums)

    

    def buble_sort(self,arr):
        for i in range(len(arr)):
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        return arr
        