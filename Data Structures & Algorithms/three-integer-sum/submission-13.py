class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.merge_sort(nums)
        n=len(nums)
        i,j,k=0,0,0
        ans=[]

        for i in range(n-2):
            if nums[i]>0:
                break

            if i>0 and nums[i]==nums[i-1]:
                continue

            j,k=i+1,n-1

            while j<k:
                total=nums[i]+nums[j]+nums[k]

                if total<0:
                    j+=1
                elif total >0:
                    k-=1

                else:
                    ans.append([nums[i], nums[j], nums[k]])
                
                    while j<k and nums[j]==nums[j+1]:
                        j+=1

                    while j<k and nums[k]==nums[k-1]:
                        k-=1


                    j+=1
                    k-=1

        return ans

    def merge_sort(self,arr):
        if len(arr)<=1:
            return arr
        l=0
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        self.merge_sort(left)
        self.merge_sort(right)


        i,j,k=l,0,0

        while j<len(left) and k<len(right):
            if left[j]<right[k]:
                arr[i]=left[j]
                j+=1

            else:
                arr[i]=right[k]
                k+=1

            i+=1

        while j<len(left):
            arr[i]=left[j]
            j+=1
            i+=1

        while k<len(right):
            arr[i]=right[k]
            k+=1
            i+=1





