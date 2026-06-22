class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        freq=[[]for i in range(len(nums)+1)]

        for n in nums:
            res[n]=1+res.get(n,0)
        for n,c in res.items():
            freq[c].append(n)
        
        ress=[]
        for i  in range(len(nums),0,-1):
            for n in freq[i]:
                ress.append(n)
                if len(ress)==k:
                    return ress


        
        