class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs=="":
            return []
        ans=defaultdict(list)

        for s in strs:
            key="".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())


        