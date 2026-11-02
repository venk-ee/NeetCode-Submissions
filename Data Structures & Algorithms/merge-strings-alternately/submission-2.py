class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=len(word1)
        w2=len(word2)
        l=0
        r=0
        res=[]
        while l<w1 and r<w2:
            res.append(word1[l])
            res.append(word2[r])
            r+=1
            l+=1
        
        while l<w1:
            res.append(word1[l])
            l+=1
        while r<w2:
            res.append(word2[r])
            r+=1

        return "".join(res)
        

        