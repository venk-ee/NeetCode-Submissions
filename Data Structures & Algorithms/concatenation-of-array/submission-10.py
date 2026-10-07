class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp=[]
        for i in range(2):
            for n in nums:
                temp.append(n)

        return temp

        