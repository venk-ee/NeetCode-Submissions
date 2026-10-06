class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}

        for num in arr:
            freq[num]=1+freq.get(num,0)

        res=-1

        for num,cnt in freq.items():
            if  num==cnt:
                res=max(res,cnt)


        return res