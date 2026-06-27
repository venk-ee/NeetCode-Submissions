class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        sett=set()

        for num  in nums:
            count[num]=1+count.get(num,0)
        for n,c in count.items():
            freq[c].append(n)
        ress=[]
        for i in range(len(nums),0,-1):
            for numss in freq[i]:
                ress.append(numss)
                if len(ress)==k:
                    return ress


            