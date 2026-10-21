class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length=min(len(s) for s in strs)
        ans=[]
        if not strs:
            return " "
        for i in range(min_length):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return "".join(ans)

                
            ans.append(s[i])

        return "".join(ans)