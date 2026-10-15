class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=min(len(i) for i in strs)

        ans=[]
        for i in range(min_len):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return "".join(ans)
            ans.append(s[i])


        return "".join(ans)
        