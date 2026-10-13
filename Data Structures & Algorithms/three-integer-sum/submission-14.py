class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i,j,k=0,0,0

        ans=[]

        for i, n in enumerate(nums):
            if n>0:
                break

            if i>0 and n==nums[i-1]:
                continue

            j,k=i+1,len(nums)-1

            while j<k:
                threesum=n+nums[j]+nums[k]

                if threesum>0:
                    k-=1

                elif threesum<0:
                    j+=1

                else:
                    ans.append([n,nums[j],nums[k]])
                    j+=1
                    k-=1

                    while nums[j]==nums[j-1]and j<k:
                        j+=1
                    while nums[j]==nums[k+1]and j<k:
                        k-=1

        return ans 

                     