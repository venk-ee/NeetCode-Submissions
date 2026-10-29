class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len=min(len(i)for i in strs)
        ans=[]
        i=0
        while i<min_len:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return "".join(ans)

            ans.append(s[i])
            i+=1

        return "".join(ans)
