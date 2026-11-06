class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k%=n

        def reverr(arr,start,end):
            l,r=start,end
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1


        
        reverr(nums,0,n-1)
        reverr(nums,0,k-1)
        reverr(nums,k,n-1)