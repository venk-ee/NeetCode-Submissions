class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        
        l=r=0
        temp=[]

        while l<l1 and r<l2:
            temp.append(word1[l])
            l+=1
            temp.append(word2[r])
            r+=1

        while l<l1:
            temp.append(word1[l])
            l+=1
        while r<l2:
            temp.append(word2[r])
            r+=1

        return "".join(temp)

