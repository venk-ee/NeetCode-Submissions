class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs :
            return " "

        ans=[]
        min_len=min(len(i) for i in strs)

        for i in range(min_len):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return "".join(ans)
                
            ans.append(strs[0][i])
        return "".join(ans)


