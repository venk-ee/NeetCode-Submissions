class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        return self._merge_sort(nums,0,len(nums)-1)
        
    def _merge(self,arr,l,m,r):
        left,right=arr[l:m+1],arr[m+1:r+1]
        i,j,k=l,0,0

        while j<len(left)and k<len(right):
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
            i+=1
            k+=1

    def _merge_sort(self,arr,l,r):
        if l>=r:
            return arr
        m=(l+r)//2
        self._merge_sort(arr,l,m)
        self._merge_sort(arr,m+1,r)
        self._merge(arr,l,m,r)

        return arr