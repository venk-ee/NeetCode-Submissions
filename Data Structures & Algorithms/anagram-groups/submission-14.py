class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return ""
        ans=defaultdict(list)

        for s in strs:
            temp="".join(sorted(s))
            ans[temp].append(s)

        return list(ans.values())
